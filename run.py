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


def user_input(ship_placement):
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
                        # Placing ship horizontally for computer
                        if orientation == "H":
                            for i in range(column + column + ship_length):
                                borad[row][i] = "X"
                            else:
                                # Placing ship vertiaclly for computer
                                for i in range(row, row +ship_length):
                                    board[i][column] = "X"
                            break
            else:
                # Placing ships for users
                ship_placement = True
                print('Place Ship With Length Of ' + str(ship_length))
                row, column, orientation = user_input(ship_placement)
                if check_ship_fits(ship_length, row, column, orientation):
                    if check_for_overlap(board, row, column, orientation, ship_length) is False:
                        if orientation == "H":
                            for i in range(column, column + ship_length):
                                board[row][i] = "X"
                        else:
                            for i in range(row, row +ship_length):
                                board[i][column] = "X"
                        print_board(user_board)
                        break

# Check for ships to ensure they don't operlap
def check_for_overlap(board, row, column, orientation, ship_length):
    if orientation == "H":
        for i in range(column, column + ship_length):
            if board[row][i] == "X":
                return True
    else:
        for i in range(row, row +ship_length):
            if board[1][column] == "X":
                return True
    return False


def check_ship_fits(ship_length, row, column, orientation):
    pass


print_board(user_board)
print_board(computer_board)
ship_placement(user_board)
ship_placement(computer_board)

"""

def hit_counter():


def turn_ability():

"""
