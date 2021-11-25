import random
"""Test file for battleships game
def start():
    print('''
 |    |    |    ______               _______    _______    __________    ______
 |    |    |   |         |          |          |       |   |    |   |   |
 |    |    |   |         |          |          |       |   |    |   |   |
 |    |    |   |------   |          |          |       |   |    |   |   |------
 |    |    |   |         |          |          |       |   |    |   |   |
 |____|____|   |______   |_______   |_______   |_______|   |    |   |   |______

    ''')


start()

"""

# H = Horizontal
# V = Vertical
# length > 9 both ways
# X = Hit ship and ship location
# O = Miss


user_board = [[" "] * 9 for i in range(9)]
user_guess_board = [[" "] * 9 for i in range(9)]
computer_board = [[" "] * 9 for i in range(9)]
computer_guess_board = [[" "] * 9 for i in range(9)]


length_of_ships = [2, 3, 4, 5, 6]
letters_to_numbers = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4,
    'F': 5, 'G': 6, 'H': 7, 'I': 8}


# Testing ways to build board

def print_board(board):
    print("  A B C D E F G H I ")
    print("  -----------------")
    row_number = 1
    for i in range(0, 9):
        board.append(['O'] * 9)
        print(row_number, "|".join(board[i]))
        row_number += 1


print_board(user_board)
