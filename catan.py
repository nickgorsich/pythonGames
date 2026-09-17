#####################################
' Catan '

import random
#####################################

def dieRoll():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    roll = (dice1 + dice2)
    roll = str(roll)
    with open('catan_rolls.txt', 'a') as rollHistory:
        rollHistory.write(f"--> {roll} \n\n")
    with open('catan_rolls.txt', 'r') as rollHistory:
        history = rollHistory.read()
    print(history)
    rollHistory.close()


def newGame():
    with open('catan_rolls.txt', 'w') as clear:
        clear.write("\nNew game \n")


def findFrequencies():
    rolls = []
    with open("catan_rolls.txt", 'r') as f:
        lines = f.readlines()
    
    for line in lines:
        if line[0] == '-':
            x = line.split(' ')
            rolls.append(int(x[1].strip()))

    rollOccurrences = {'2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0}
    for roll in rolls:
        rollOccurrences[str(roll)] += 1
    
    keys = []
    for key in rollOccurrences.keys():
        keys.append(key)
    counts = []
    for count in rollOccurrences.values():
        counts.append(count)

    prints = []
    for i in range(len(keys)):
        x = f'{keys[i]}: {counts[i]}'
        prints.append(x)
    
    pairs = []
    for i in range(len(keys)):
        pairs.append([counts[i], keys[i]])

    print('\nNumber Frequencies: \n')
    for line in prints:
        print(line)

    print()
    return pairs


def sortedFrequencies(pairs):
    sortedPairs = sorted(pairs)
    sortedPairs.reverse()

    print('\nRoll Frequencies, Sorted: \n')
    for i in range(len(pairs)):
        print(f'{sortedPairs[i][1]}: {sortedPairs[i][0]}')


' ========================== Main Program  ============================ '

# newGame()

dieRoll()

# sortedFrequencies(findFrequencies())
