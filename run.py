# python code goes here

length_of_ships = [2, 3, 4, 5, 6]
user_board = [[" "] * 9 for i in range(9)]


def print_board(board):
    """
    A function for creating the gameboards
    for the user, computer and guessboards
    """
    print("  A B C D E F G H I")
    print("  __________________")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
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
