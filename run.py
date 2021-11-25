"""
Keys
V = Vertical
H = Horizontal

X = Hit
O = Miss
"""


letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8
    }

length_of_ships = [2, 3, 4, 5, 6]
user_board = [[" "] * 9 for i in range(9)]
user_guess_board = [[" "] * 9 for i in range(9)]

computer_board = [[" "] * 9 for i in range(9)]
computer_guess_board = [[" "] * 9 for i in range(9)]


def name():
    """
    A function for getting the user's name
    """
    username = str(input("Enter Your Name: "))
    print("Welcome To Battleships " + str(username))
    return


def print_board(board):
    """A function for building all game boards
    for battleships"""
    print("  A B C D E F G H I ")
    print("  -----------------")
    row_number = 1
    for i in range(0, 9):
        board.append(['O'] * 9)
        print(row_number, "|".join(board[i]))
        row_number += 1


print_board(user_board)
"""

def place_ships():


def check_ship_fits():


def check_for_overlap():


def user_input():


def hit_counter():


def turn_ability():

"""
