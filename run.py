"""
Battleships Game
"""
import random


# Keys
# V = Vertical
# H = Horizontal

# X = Hit
# O = Miss

# Letters to numbers function taken from elsewhere
# Check readme
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

length_of_ships = [1, 2, 3, 4, 5]
user_board = [[" "] * 9 for i in range(9)]
user_guess_board = [[" "] * 9 for i in range(9)]

computer_board = [[" "] * 9 for i in range(9)]
computer_guess_board = [[" "] * 9 for i in range(9)]


def start():
    """
    Function for welcome message
    """
    print('''
 |    |    |    ______               _______    _______    __________    ______
 |    |    |   |         |          |          |       |   |    |   |   |
 |    |    |   |         |          |          |       |   |    |   |   |
 |    |    |   |------   |          |          |       |   |    |   |   |------
 |    |    |   |         |          |          |       |   |    |   |   |
 |____|____|   |______   |_______   |_______   |_______|   |    |   |   |______

    ''')


start()


def name():
    """
    A function for getting the user's name
    """
    username = str(input("Choose What We Call You, Or Just Press Enter:\n "))
    print("Welcome To Battleships " + str(username))
    return


name()


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
                orientation, row, column = random.choice(
                    ["H", "V"]), random.randint(0, 8), random.randint(0, 8)
                if check_ship_fits(ship_length, row, column, orientation):
                    overlaps = check_for_overlap(board,
                                                 row,
                                                 column,
                                                 orientation,
                                                 ship_length)
                    if overlaps is False:
                        # Placing ship horizontally for computer
                        if orientation == "H":
                            for i in range(column,  column + ship_length):
                                board[row][i] = "X"
                        else:
                            # Placing ship vertiaclly for computer
                            for i in range(row, row + ship_length):
                                board[i][column] = "X"
                        break
            else:
                # Placing ships for users
                ship_placement = True
                print('Place Ship With Length Of ' + str(ship_length))
                row, column, orientation = user_input(ship_placement)
                if check_ship_fits(ship_length, row, column, orientation):
                    if check_for_overlap(board, row,
                                         column, orientation,
                                         ship_length) is False:
                        if orientation == "H":
                            for i in range(column, column + ship_length):
                                board[row][i] = "X"
                        else:
                            for i in range(row, row + ship_length):
                                board[i][column] = "X"
                        print_board(user_board)
                        break


# Checking if ship fits on game grid
def check_ship_fits(ship_length, row, column, orientation):
    """Function for checking ships are being places¨
    in a location that fits"""
    if orientation == "H":
        if column + ship_length > 9:
            return False
        else:
            return True
    else:
        if row + ship_length > 9:
            return False
        else:
            return True


# Check for ships to ensure they don't operlap
def check_for_overlap(board, row, column, orientation, ship_length):
    """
    A function to check that ships don't operlap eachother
    """
    if orientation == "H":
        for i in range(column, column + ship_length):
            if board[row][i] == "X":
                return True
    else:
        for i in range(row, row + ship_length):
            if board[1][column] == "X":
                return True
    return False


def user_input(ship_placement):
    """
    User input for choosing where to place their ships
    """
    if ship_placement is True:
        while True:
            try:
                orientation = input(
                    "Choose Orientation H(orizontal) Or V(ertical):\n").upper()
                if orientation == "H" or orientation == "V":
                    break
            except KeyError:
                print("INVALID Input Choose H Or V")
        while True:
            try:
                row = input("Enter Row Number Between 1 And 9:\n ")
                if row in '123456789':
                    row = int(row) - 1
                    break
            except ValueError:
                print('INVALID Input, Choose Between 1 And 9')
        while True:
            try:
                column = input("Choose A Column Between A And I:\n ").upper()
                if column in 'ABCDEFGHI':
                    column = letters_to_numbers[column]
                    break
            except KeyError:
                print('INVALID, Choose Between A And I')
        return row, column, orientation
    else:
        while True:
            try:
                row = input("Enter Row Number Between 1 And 9:\n ")
                if row in '123456789':
                    row = int(row) - 1
                    break
            except ValueError:
                print('INVALID Input, Choose Between 1 And 9')
        while True:
            try:
                column = input("Choose A Column Between A And I:\n ").upper()
                if column in 'ABCDEFGHI':
                    column = letters_to_numbers[column]
                    break
            except KeyError:
                print('INVALID, Choose Between A And I')
        return row, column


def hit_counter(board):
    """Function for counting hits for both user and computer"""
    counter = 0
    for row in board:
        for column in row:
            if column == "X":
                counter += 1
    return counter


def turns(board):
    """A function for both user turns
    and computer turns"""
    if board == user_guess_board:
        row, column = user_input(user_guess_board)
        if board[row][column] == "O":
            turns(board)

        elif board[row][column] == "X":
            turns(board)
        elif computer_board[row][column] == "X":
            board[row][column] = "X"
        else:
            board[row][column] = "O"
    else:
        row, column = random.randint(0, 8), random.randint(0, 8)
        if board[row][column] == "O":
            turns(board)
        elif board[row][column] == "X":
            turns(board)
        elif user_board[row][column] == "X":
            board[row][column] = "X"
        else:
            board[row][column] = "O"


ship_placement(computer_board)
print_board(computer_guess_board)
ship_placement(user_board)
print_board(user_board)


while True:
    # Player Turn
    while True:
        print('Your Guesses Are Recorded Below')
        print('X Means Hit, O Is For Miss, Good Luck')
        print_board(user_guess_board)
        turns(user_guess_board)
        break
    if hit_counter(user_guess_board) == 15:
        print("Yaay, You Won!! ")
        break
    # Computer Turn
    while True:
        turns(computer_guess_board)
        break
    print_board(computer_guess_board)
    if hit_counter(computer_guess_board) == 15:
        print("HaHa, You Lose!! Press Reset To Play Again")
        break
