'''
    build_wordlists.py
    Made by Nicholas Gorsich
    All rights reserved. 2026

    Regenerates words.json (the answer pool) from dictionary.json (every valid
    5-letter word). Run it after editing dictionary.json or the tuning knobs
    below -- the game files themselves never need to change.

        python3 build_wordlists.py            # rewrite words.json
        python3 build_wordlists.py --dry-run  # just report what would change

    No installs needed: how common each word is comes from word_frequency.json,
    a table baked in next to this script.

    Three filters run in order:
      1. plurals / "-s" verb forms  ->  abets, tacos, tries, boxes
      2. corpus rarity below ZIPF_MIN  ->  abaca, abend, aargh
      3. MANUAL_DROP, the hand-curated list at the bottom of this file
'''

import json     # read and write the word lists
import os       # locate the json files next to this script
import sys      # --dry-run flag


''' TUNING '''

# Zipf scale: 6 = "the", 4 = "house", 3 = "quartz", 2 = obscure.
# Lower this for a bigger answer pool, raise it for a more common one.
# 2.8 -> roughly 2000 words, 2.4 -> roughly 2300, 2.2 -> roughly 2500.
ZIPF_MIN = 2.4

# Stems are only treated as real words above this, so "abets" loses to "abet"
# but "bonus" survives ("bonu" scores nothing).
STEM_ZIPF_MIN = 3.2

HERE = os.path.dirname(os.path.abspath(__file__))
DICTIONARY = os.path.join(HERE, 'dictionary.json')
WORDS = os.path.join(HERE, 'words.json')
FREQUENCIES_PATH = os.path.join(HERE, 'word_frequency.json')

# 1913 Webster's, shipped with macOS. Used to tell real words from corpus noise
# and to spot proper nouns (listed capitalized only).
WEB2 = '/usr/share/dict/web2'
PROPERNAMES = '/usr/share/dict/propernames'


''' LEXICONS '''

def load_lexicons():
    lower, upper, proper = set(), set(), set()

    if os.path.exists(WEB2):
        for raw in open(WEB2):
            entry = raw.strip()
            if entry.islower():
                lower.add(entry)
            elif entry[:1].isupper():
                upper.add(entry.lower())

    if os.path.exists(PROPERNAMES):
        for raw in open(PROPERNAMES):
            proper.add(raw.strip().lower())

    return lower, upper, proper


LOWER, UPPER, PROPER = load_lexicons()

with open(FREQUENCIES_PATH, 'r') as f:
    FREQUENCIES = json.load(f)

unscored = set()   # words the baked-in table has never heard of


''' FILTERS '''

def frequency(word):
    '''
    Zipf score from the baked-in table: 6 = "the", 4 = "house", 3 = "quartz".
    A word the table is missing scores 0, which reads as "nobody uses this" --
    see regenerate() at the bottom if you add such words to the dictionary.
    '''
    if word in FREQUENCIES:
        return FREQUENCIES[word]
    unscored.add(word)
    return 0.0


def isWord(stem):
    ''' Is this stem a real, reasonably known English word? '''
    return len(stem) >= 3 and (stem in LOWER or frequency(stem) >= STEM_ZIPF_MIN)


def isPlural(word):
    ''' Plural noun or third-person-singular verb form. '''
    if not word.endswith('s'):
        return False
    if word.endswith(('ss', 'us', 'is')):    # chess, focus, basis
        return False
    if word.endswith('ies') and isWord(word[:-3] + 'y'):   # tries -> try
        return True
    if word.endswith(('ches', 'shes', 'xes', 'zes')) and isWord(word[:-2]):   # boxes -> box
        return True
    if isWord(word[:-1]):                    # tacos -> taco
        return True
    if word.endswith('es') and isWord(word[:-2] + 'e'):
        return True
    return False


def isProperNoun(word):
    ''' Listed capitalized in the dictionary, never lowercase. '''
    return (word in UPPER or word in PROPER) and word not in LOWER


def curate(dictionary):
    ''' dictionary -> (answer pool, {dropped word: reason}) '''
    manual = manualDrops()
    keep, dropped = [], {}

    for word in dictionary:
        score = frequency(word)

        if isPlural(word):
            dropped[word] = 'plural'
        elif isProperNoun(word):
            dropped[word] = 'proper noun'
        elif score < ZIPF_MIN:
            dropped[word] = 'rare (%.2f)' % score
        elif word in manual:
            dropped[word] = 'manual'
        else:
            keep.append(word)

    return sorted(keep), dropped


def manualDrops():
    words = set()
    for line in MANUAL_DROP.splitlines():
        line = line.strip()
        if line and not line.startswith('#'):
            words.update(line.split())
    return words


''' FILE IO '''

def writeList(path, words):
    ''' 10 words per line so the diffs stay readable. '''
    with open(path, 'w') as f:
        f.write('[\n')
        for i in range(0, len(words), 10):
            row = ', '.join('"%s"' % w for w in words[i:i + 10])
            f.write('  ' + row + (',' if i + 10 < len(words) else '') + '\n')
        f.write(']\n')


def main():
    if '--refresh' in sys.argv:
        regenerate()
        return

    dryRun = '--dry-run' in sys.argv

    with open(DICTIONARY, 'r') as f:
        dictionary = sorted(json.load(f))

    keep, dropped = curate(dictionary)

    reasons = {}
    for reason in dropped.values():
        reason = reason.split(' (')[0]
        reasons[reason] = reasons.get(reason, 0) + 1

    print("dictionary.json : %d words" % len(dictionary))
    for reason in sorted(reasons):
        print("  - %-11s %d" % (reason, reasons[reason]))
    print("words.json      : %d words" % len(keep))

    if unscored:
        missing = sorted(w for w in unscored if len(w) == 5)
        if missing:
            print("\nnot in word_frequency.json, so treated as rare: "
                  + ', '.join(missing[:20])
                  + (' ...' if len(missing) > 20 else ''))
            print("see regenerate() below to score them")

    if dryRun:
        print("\n(dry run, nothing written)")
        return

    writeList(WORDS, keep)
    print("\nwrote " + WORDS)


''' REBUILDING THE FREQUENCY TABLE

word_frequency.json covers every word in dictionary.json as of the day it was
built, so day to day this script needs nothing installed. Only if you add new
words to the dictionary and want them scored do you need wordfreq, and Homebrew
python refuses to install into itself, so it has to go in a throwaway venv:

    python3 -m venv /tmp/freq && /tmp/freq/bin/pip install wordfreq
    /tmp/freq/bin/python build_wordlists.py --refresh

Until then, an unscored word just counts as rare and stays out of the answer
pool -- the games keep working either way.
'''

def regenerate():
    from wordfreq import zipf_frequency   # only needed for --refresh

    with open(DICTIONARY, 'r') as f:
        words = sorted(json.load(f))

    needed = set(words)
    for word in words:                    # every stem isPlural() can ask about
        if word.endswith('s') and not word.endswith(('ss', 'us', 'is')):
            needed.add(word[:-1])
            if word.endswith('ies'):
                needed.add(word[:-3] + 'y')
            if word.endswith('es'):
                needed.add(word[:-2])
                needed.add(word[:-2] + 'e')

    table = [(w, round(zipf_frequency(w, 'en'), 2))
             for w in sorted(needed) if len(w) >= 3]

    with open(FREQUENCIES_PATH, 'w') as f:
        f.write('{\n')
        for i in range(0, len(table), 6):
            row = ', '.join('"%s": %s' % pair for pair in table[i:i + 6])
            f.write('  ' + row + (',' if i + 6 < len(table) else '') + '\n')
        f.write('}\n')

    print("wrote %s (%d entries)" % (FREQUENCIES_PATH, len(table)))


''' HAND-CURATED REMOVALS

Words the automatic filters keep but that make bad answers: brands, proper
nouns, foreign phrase fragments, slang, British-only spellings, jargon, slurs,
and anything most people would not recognize. Add to it freely -- a word listed
here that is not in the dictionary is harmless.
'''

MANUAL_DROP = '''
# irregular / missed plurals
buses bytes cacti cilia curia dorks elves feces fungi gases geese gurus kiwis labia larva
menus minis orcas pubes radii saris semis septa taxis women

# slang, contractions, txt-speak
ahhhh aunty bimbo boner bubba busty chink decaf dicky diddy dildo dilly doggo dovey dunno
fella gimme golly gonna gotta hallo honky howdy hubby kinda lemme lordy mamma mammy merch
momma ohhhh outta pappy porno raped sicko smurf snark sorta squaw telly thanx tippy titty
vocab vroom wahoo wanna welch wench wifey yikes

# foreign words / phrase fragments
adios afore altho alway annum aught avant bonne buena bueno campo canto carne cotta culpa
cuppa didst dixit dolce duomo durst ennui etude facto faire fatwa femme firma forma garde
grata hamza haute homme intra kappa lapis largo laude lemma lexis livre magna magus marge
masse mater mezzo mucho mufti neath noire ochre ombre paean pasha passe pater plein polis
prima primo rajah sabra sahib saith selah shalt shiki sigma solon spake supra sutra swami
taxon terra theta thine torah tutti utero versa verso vitae vitro vivre xenia zooey

# brands / proper nouns
anglo astro bowie curie degas delft droid fermi gabby ginny intel kraft lacey laker libra
lycra mavis melba petri razer rowan sarge tesla twain xerox

# British / variant spellings
enrol fibre gipsy litre metre mould nosey odour payed sabre wooly

# chemistry / technical / jargon
alkyl amide amine anion borer boron boson butyl calyx codon conic dimer edema ester ethyl
folic fossa fosse gauss glans hymen joule lumen nodal phage redox redux staph strep tetra
torus tubal tuple whorl zonal

# obscure or archaic
actin aegis afoul agora ahold algal ambit amity anima anise apace arras ascot assed augur
aural avast baldy bally bandy basso batik bazar beaut beaux bebop begat belay belli beryl
betel bight bilge biter bitty boggy bogie bonny bossa brant bream bruin busby butch butte
buzzy canna carer caron carte cased cheep chine chino clack comer coney covey cress crick
crier croft crone crump curio daffy dally datum dinar divan djinn doozy dotty dowdy dower
droll duchy ducky duper dusky eared egged elegy emery ender facie fader fecal feint filer
firth fitch fiver flack flume furor genet glebe gonzo grist gronk guano gulag hocus hokey
holed hooch hoppy hosed idyll imbue infra inlay islet jawed jokey junky kiddy kneed krone
laird laity larch laver leant leggy liege lifer liken lisle liven lobed lolly mange manna
manse matey maven mealy meted miler mitre modus mondo morel moxie mumbo mused musky narco
nitty nonce nosed olden ortho ovate ovoid pacer paged pally peaky pease petit piney playa
plied posit prise purer quint ravel rayed rebar rebus recon reedy reeve refit retry riven
robed rondo roper rosin ruble sager sated satyr saver sayer scion scrim scrip seine serge
serif servo sexed shank sheik shied shill shire shorn sibyl sired sited skeet skied skint
sloop smock snafu snook sooty sowed spate spelt spina spitz stave summa swain synch synod
tabor tarry tater thane thunk toddy tonal toyed trice trier trike tuber tulle twill twink
unlit unmet unsee upped usury vapid ville washy whist wilco
'''


''' FUNCTION CALLS '''

main()
