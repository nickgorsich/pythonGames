###################################### SETUP

import os # for colors
import time # for sleep

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

os.system("") # open color mode in terminal

board = [' ', ' ', ' ', # initiate board
         ' ', ' ', ' ',
         ' ', ' ', ' ']

####################################### FUNCTIONS

def color_symbol(cell): # coloring X red and O blue
    if cell == 'X':
        return style.RED + 'X' + style.RESET
    elif cell == 'O':
        return style.BLUE + 'O' + style.RESET
    else:
        return ' '

def display(): # displays board
    
    print(f" {color_symbol(board[0])} │ {color_symbol(board[1])} │ {color_symbol(board[2])} ")
    print("───┼───┼───")
    print(f" {color_symbol(board[3])} │ {color_symbol(board[4])} │ {color_symbol(board[5])} ")
    print("───┼───┼───")
    print(f" {color_symbol(board[6])} │ {color_symbol(board[7])} │ {color_symbol(board[8])} ")


def check_winner():
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # horizontal
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # vertical
        (0, 4, 8), (2, 4, 6)             # diagonal
    ]

    for combo in winning_combinations:

        # checks all winning combos, for each combo if all three positions are the same symbol and not empty 
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ': 
            return board[combo[0]] # return the winning symbol 

    return None


def is_board_full():
    return ' ' not in board


symbols = ['X', 'O']

turn = 0

####################################### GAME LOOP

while True:
    os.system("cls") # clear terminal

    # print title and instructions
    print(style.CYAN + "\nNick's Tic Tac Toe\n" +
      style.BLACK + "Enter [q] to quit\n" +
      style.RESET + "\nLocations on the board:\n")

    print( # board locations
        " 1 │ 2 │ 3\n"
        "───┼───┼───\n"
        " 4 │ 5 │ 6\n"
        "───┼───┼───\n"
        " 7 │ 8 │ 9\n" )

    print(style.BLACK + "-----------" + style.RESET)
    display()
    print(style.BLACK + "-----------" + style.RESET)


    # actual gameplay

    move = input(style.YELLOW + f"Player {symbols[turn % 2]}'s turn. Choose a position (1-9): " + style.RESET)

    if move == 'q':
        print(style.MAGENTA + "Game exited." + style.RESET) # quit option
        break

    if move.isdigit():
        move = (int(move) - 1) # convert to 0-indexed

        if move < 0 or move > 8 or board[move] != ' ': # ensure move is valid number and location is empty
            print(style.RED + "Invalid move. Try again." + style.RESET)
            time.sleep(1)
            continue

        board[move] = symbols[turn % 2]

        winner = check_winner()

        if winner:
            os.system("cls") # clear terminal
            display()
            print(style.GREEN + f"Player {winner} wins!" + style.RESET)
            break

        if is_board_full():
            os.system("cls") # clear terminal
            display()
            print(style.CYAN + "It's a draw!" + style.RESET)
            break

        turn += 1

    else: # invalid input check
        print(style.RED + "Invalid input. Enter a number between 1–9." + style.RESET)
        continue