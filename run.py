import random
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


def user_input():
    """
    User input for choosing where to place their ships
    """
    column = input("Select A Column Between A and I: ").upper()
    while column not in "ABCDEFGHI":
        print("Incorrect Input, Pick Between A and I")
        column = input("Select A Column Between A and I:").upper()
    row = input("Select A Row Between 1 - 9: ")
    while row not in "123456789":
        print("Incorrect Input, Pick Between 1 And 9 ")
        row = input("Select A Row Between 1-9: ")


def ship_placement(board):
    """
    Function for users placing their ships on the game board
    and randomize ship placement for computer
    """
    # Loops through all ships
    for ship_length in length_of_ships:
        while True:
            # Randomly places ships for computer
            if board == computer_board:
                orientation, row, column = random.choice(["H", "V"]), random.randint(0, 8), random.randint(0, 8)
                if check_ship_fits(ship_length, row, column, orientation):
                    overlaps = check_for_overlap(board, row, column, orientation, ship_length)
                    if overlaps is False:
                        # Placing ship horizontally
                        if orientation == "H":
                            for i in range(column + column + ship_length):
                                borad[row][i] = "X"
                            else:
                                # Placing ship vertiaclly
                                for i in range(row, row +ship_length):
                                    board[i][column] = "X"
                            break




def check_ship_fits(ship_length, row, column, orientation):
    pass


print_board(user_board)
user_input()
"""







def check_for_overlap():


def user_input():


def hit_counter():


def turn_ability():

"""
