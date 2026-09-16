''' 
    Wordle.py
    Made by Nicholas Gorsich
    All rights reserved. 2026
'''

# see old version on HP to add TIME and other COMMENTS and more visuals for terminal

import random   # word selection
import time     # time each game and output upon completion
import os       # add terminal clear commands
import json     # load word list from json file

class Style:
    Green = '\033[92m'
    Yellow = '\033[93m'
    White = '\033[97m'
    Reset = '\033[0m'

wordList = []
with open('words.json', 'r') as f:
    wordList = json.load(f)
# wordList = ['audio', 'frame', 'prone', 'stink', 'death']

def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def win():
    print('Correct!')

def gameOver():
    print(f'Answer = {answer}. Game over.')


answer = random.choice(wordList)
attempts = 0

while attempts < 6:
    guess = input('--> ').strip().lower()

    if len(guess) != 5 or guess not in wordList:
        print('Enter a five-letter word from the word list.')
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

    if guess == answer:
        win()

gameOver()