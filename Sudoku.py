"""
Author: Edgar Argueta
Filename: Sudoku.py
"""
import random

ROWS = 9
COLS = 9
BOARD = [[0 for i in range(ROWS)] for j in range(COLS)]
EASY_MODE = 38
INTERMEDIATE_MODE = 30
HARD_MODE = 24
EXPERT_MODE = 17

def print_board():
    print()
    for x in range(ROWS):
        print("\t", end='')
        for y in range(COLS):
            print(BOARD[x][y], end=' ')
        print()


def check_row(num, row, col):
    for y in range(COLS):
        if y != col:
            if BOARD[row][y] == num:
                return False
    return True


def check_col(num, row, col):
    for x in range(ROWS):
        if x != row:
            if BOARD[x][col] == num:
                return False
    return True


def check_square(num, row, col):
    start_x = row - (row % 3)
    start_y = col - (col % 3)
    for x in range(start_x,start_x+3):
        for y in range(start_y, start_y+3):
            if x != row and y != col:
                if BOARD[x][y] == num:
                    return False
    return True


def check_all(num, row, col):
    if check_col(num, row, col) and check_col(num, row, col) and check_square(num, row, col):
        return True
    return False


def create_sudoku(mode):
    count = 81 - mode
    unused_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        test_num = random.choice(unused_num)
        unused_num.remove(test_num)
        BOARD[0][i] = test_num

    for x in range(1, 9):
        shift = 3
        if x == 3 or x == 6:
            shift = 1
        for y in range(COLS):
            BOARD[x][y-shift] = BOARD[x-1][y]

    while count != 0:
        row = random.randint(ROWS)
        col = random.randint(COLS)
        if BOARD[row][col] == '.':
            continue
        BOARD[row][col] = '.'
        count -= 1


def find_empty():
    for x in range(ROWS):
        for y in range(COLS):
            if BOARD[x][y] == '.':
                return True
    return False





def main():
    create_sudoku(EASY_MODE)
    print_board()


if __name__ == '__main__':
    main()
