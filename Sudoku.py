"""
Author: Edgar Argueta
Filename: Sudoku.py
"""
import random

ROWS = 9
COLS = 9
BOARD = [[0 for i in range (ROWS)] for j in range (COLS)]


def print_board():
    print()
    for x in range (ROWS):
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


def main():
    BOARD[1][5] = 5
    BOARD[3][5] = 5
    BOARD[0][2] = 3
    BOARD[0][7] = 5
    if check_col(5, 0, 5):
        print("FAILURE #1")
    if check_col(3, 0, 2):
        print("SUCCESS #1")
    if check_row(5, 1, 5):
        print("FAILURE #2")
    if check_row(3, 0, 2):
        print("SUCCESS #2")
    print_board()


if __name__ == '__main__':
    main()
