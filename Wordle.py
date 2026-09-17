''' 
    Wordle.py
    Made by Nicholas Gorsich
    All rights reserved. 2026
'''

# Features to add
# 
# 0.  Rename variables to be more descriptive and easier to read.
# 1.  Visualize the letters that have been guessed and their colors 
#     (green, yellow, white) in a keyboard layout format.
# 2.  Same name leaderboard entries should be combined into one entry 
#     with the best score (lowest time and attempts) displayed.
# 2.5 Determine weight of attempts vs time for leaderboard ranking.
# 3.  Switch from colored text to colored blocks for clearer visual.
# 4.  Reset terminal more often, clear "not a word" and other temporary messages
#     such as hints or attempts left. 
# 5.  Add easter eggs


import random   # word selection
import time     # time each game and output upon completion
import os       # add terminal clear commands
import json     # load word list from json file


class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    GREY = '\033[90m'

def clearTerminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

os.system("")
clearTerminal()

wordList = []
with open('words.json', 'r') as f:
    wordList = json.load(f)

dictionary = []
with open('dictionary.json', 'r') as f:
    dictionary = json.load(f)

def Wordle():
    answer = random.choice(wordList).upper()
    print(style.MAGENTA + "\n -- Welcome to Nick's Wordle --" + style.RESET)
    print(style.BLUE + "  - Enter [quit] to end game -" + style.RESET)
    print(style.BLUE + "  - Enter [hint] for a hint -" + style.RESET)
    name = input("Enter your name: ")
    if name == "":
        name = "Anonymous"
    if name == "quit":
        print(style.GREY + "loser!" + style.RESET)
        time.sleep(1)
        quit()

    initialTime = time.time()  # game start

    print(style.CYAN + "Guess below. You have 6 attempts" + style.RESET)
    attempts = 0

    while attempts < 6:
        a = list(input("--> "))
        b = ''
        for i in a:
            b += i
        stringGuess = ''

        if a == list("quit"):
            print(style.GREY + "loser!" + style.RESET)
            time.sleep(1)
            attempts += 6
	
        elif a == list("nigga"):
            print(style.RED + "AHHH DONT ROB ME!!!" + style.RESET)
            time.sleep(1)
            attempts += 6

        elif a == list("hint"):
            options = [1, 2, 3, 4, 5]
            hint = random.choice(options)
            attempts -= 1
            if hint == 1:
                print(style.YELLOW + f"The word starts with {answer[0]}" + style.RESET)
            elif hint == 2:
                print(style.YELLOW + f"The word ends with {answer[4]}" + style.RESET)
            else:
                print(style.YELLOW + f"The word has a {answer[random.randint(0, 4)]} in it" + style.RESET)
            time.sleep(1)

        elif len(a) == 5 and b.lower() in dictionary:
            guess = [None] * 5  # store styled guess letters
            correctLetters = []
            count = 0

            # --- Count how many times each letter appears in the answer ---
            letter_counts = {}
            for ch in answer:
                ch = ch.upper()
                if ch in letter_counts:
                    letter_counts[ch] += 1
                else:
                    letter_counts[ch] = 1

            # --- First pass: mark greens and reduce letter counts ---
            for i in range(5):
                if a[i].upper() == answer[i].upper():
                    guess[i] = style.GREEN + a[i].upper() + " " + style.RESET
                    count += 1
                    correctLetters.append(a[i])
                    letter_counts[a[i].upper()] -= 1  # mark usage of this letter

            # --- Second pass: mark yellows and whites ---
            for i in range(5):
                if guess[i] is not None:
                    continue  # already marked green
                upper_letter = a[i].upper()
                if upper_letter in letter_counts and letter_counts[upper_letter] > 0:
                    guess[i] = style.YELLOW + upper_letter + " " + style.RESET
                    letter_counts[upper_letter] -= 1  # mark usage
                else:
                    guess[i] = style.WHITE + upper_letter + " " + style.RESET  # not in word

            if count == 5:
                for letter in guess:
                    stringGuess += letter
                print("--> " + stringGuess)
                time.sleep(1)
                print("Correct")
                finalTime = int(time.time() - initialTime)
                attempts += 1
                print(style.BLUE + f"It took you {finalTime} seconds and {attempts} attempts.\n" + style.RESET)
                time.sleep(1.5)

                with open('leaderboard.txt', 'a') as leaderboard:
                    leaderboard.write(f"{name}: {finalTime} seconds in {attempts} attempts.\n")

                sort_leaderboard()  # sort the leaderboard after each game
                print(style.MAGENTA + "      -- Leaderboard --\n" + style.RESET)

                with open('leaderboard.txt', 'r') as leaderboard:
                    print(leaderboard.read())  # leaderboard print statement

                z = input("Do you want to play again?: ")
                if z.lower() in ("yes", "y"):
                    clearTerminal() # clear terminal for new game
                    Wordle()
                else:
                    print(style.CYAN + "Thanks for playing" + style.RESET)
                    quit()

            for letter in guess:
                stringGuess += letter
            print("--> " + stringGuess)

        else:
            if len(a) != 5:
                print(style.GREY + "not 5 letters" + style.RESET)
            if b.lower() not in dictionary:
                print(style.GREY + "not a word" + style.RESET)

            attempts -= 1
            print(style.RED + f"Attempts left: {5 - attempts}" + style.RESET)
            time.sleep(1)

        attempts += 1

    print("Answer: " + style.GREEN + answer.upper())
    print(style.RED + "Game Over" + style.RESET)

    v = input("Do you want to play again?: ")
    if v.lower() in ("yes", "y"):
        clearTerminal()
        Wordle()
    else:
        print(style.CYAN + "Thanks for playing" + style.RESET)
        quit()


def clearleaderboard():
    with open('leaderboard.txt', 'w') as lb:
        lb.write('')

def sort_leaderboard():
    entries = []

    # -------- read and parse every line --------
    with open('leaderboard.txt', 'r') as lb:
        for raw in lb:
            line = raw.strip()
            if not line:
                continue

            # 1) remove a leading rank like "3. "
            if line[0].isdigit() and '. ' in line:
                line = line.split('. ', 1)[1]

            # 2) require the colon that separates name and score
            if ':' not in line:
                continue

            name_part, rest = line.split(':', 1)
            name = name_part.strip()

            try:
                # pull out “52” from  "52 seconds in 4 attempts."
                time_val = int(rest.split('seconds')[0].strip())
                # pull out “4”   from  "… in 4 attempts."
                attempts_val = int(
                    rest.split('in')[1].split('attempt')[0].strip()
                )
            except (IndexError, ValueError):
                continue  # malformed line → ignore

            # key order: time, then attempts, then name
            entries.append((time_val, attempts_val, name))

    # -------- sort & rewrite --------
    entries.sort()   # ascending by time, then attempts automatically
    with open('leaderboard.txt', 'w') as lb:
        for rank, (t, att, n) in enumerate(entries, start=1):
            lb.write(f"{rank}. {n}: {t} seconds in {att} attempts.\n")
    
def seeLeaderboard():
    clearTerminal()
    print(style.MAGENTA + "\n      -- Leaderboard --\n" + style.RESET)
    with open('leaderboard.txt', 'r') as leaderboard:
        print(leaderboard.read())  # leaderboard print statement


''' FUNCTION CALLS '''

Wordle()

# seeLeaderboard()

# clearleaderboard()
