''' 
    ogWordle.py
    Made by Nicholas Gorsich
    All rights reserved. 2026
'''

import random   # word selection
import time     # time each game and output upon completion
import os       # add terminal clear commands
import json

class Style:
    Green = '\033[92m'
    Yellow = '\033[93m'
    White = '\033[97m'
    Reset = '\033[0m'
    Red = '\033[91m'

    # unused currently
    Cyan = '\033[96m'
    Purple = '\033[95m'
    Blue = '\033[94m'


# wordList -> words the game can pick as the answer (common, non-plural)
# dictionary -> every valid 5-letter word, used only to validate guesses
with open('words.json', 'r') as f:
    wordList = json.load(f)

with open('dictionary.json', 'r') as f:
    dictionary = set(json.load(f))


def Wordle():
    answer = random.choice(wordList)
    attempts = 0

    while attempts < 6:
        guess = input('--> ').strip().lower()

        if len(guess) != 5 or guess not in dictionary:
            print('Enter a real five-letter word.')
            continue

        attempts += 1
        colors = [Style.White] * 5
        remaining = list(answer)

        # Mark greens and remove those letters from consideration.
        for i in range(5):
            if guess[i] == answer[i]:
                colors[i] = Style.Green
                remaining[i] = None

        # Mark yellows using only the remaining answer letters.
        for i in range(5):
            if colors[i] != Style.Green and guess[i] in remaining:
                colors[i] = Style.Yellow
                remaining[remaining.index(guess[i])] = None

        result = ''
        for i in range(5):
            result += colors[i] + guess[i].upper() + Style.Reset

        print('--> ' + result)

        if guess == answer: # winner winner chicken dinner
            print(Style.Green + 'Correct!' + Style.Reset)
            playAgain()

    # womp womp
    print(Style.Red + f'Answer = {answer}. Game over.' + Style.Reset)
    playAgain()


def clearTerminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def playAgain():
    q = input("Do you want to play again? (y/n): ").strip().lower()
    if q == 'y':
        clearTerminal()
        Wordle()
    elif q == 'n':
        print(Style.Purple + "Thanks for playing!" + Style.Reset)
        time.sleep(1)
        quit()
    else:
        print(Style.Red + "Invalid input" + Style.Reset)
        time.sleep(1)
        quit()

Wordle()