''' 
    Wordle.py
    Made by Nicholas Gorsich
    All rights reserved. 2026
'''

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


def Wordle():
    answer = random.choice(wordList).upper()
    print(style.BLUE + "\n -- Welcome to Nick's Wordle --" + style.RESET)
    print(style.MAGENTA + "  - Enter [quit] to end game -" + style.RESET)
    name = input("Enter your name: ")
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
            print(style.BLACK + "loser!" + style.RESET)
            time.sleep(1)
            attempts += 10

        elif len(a) == 5 and b.lower() in wordList:
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
                if z.lower() == "yes":
                    clearTerminal() # clear terminal for new game
                    Wordle()
                else:
                    print(style.BLACK + "Thanks for playing" + style.RESET)
                    quit()

            for letter in guess:
                stringGuess += letter
            print("--> " + stringGuess)

        else:
            if len(a) != 5:
                print(style.BLACK + "not 5 letters" + style.RESET)
            if b.lower() not in wordList:
                print(style.BLACK + "not a word" + style.RESET)

            attempts -= 1
            print(style.RED + f"Attempts left: {5 - attempts}" + style.RESET)
            time.sleep(1)

        attempts += 1

    print(style.BLACK + "Answer: " + style.GREEN + answer.upper())
    print(style.RED + "Game Over" + style.RESET)

    v = input("Do you want to play again?: ")
    if (v.lower() == "yes"):
        clearTerminal()
        Wordle()
    if (v.lower() == "y"):
        clearTerminal()
        Wordle()
    else:
        print(style.BLACK + "Thanks for playing" + style.RESET)
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
    


#clearleaderboard()

''' THE GAME STARTS HERE '''

Wordle()