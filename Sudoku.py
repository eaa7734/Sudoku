"""
Author: Edgar Argueta
Filename: Sudoku.py
"""
import random

ROWS = 9
COLS = 9
BOARD = [[0 for i in range(ROWS)] for j in range(COLS)]

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


def main():
    BOARD[1][5] = 5
    BOARD[3][5] = 5
    BOARD[0][2] = 3
    BOARD[0][7] = 5
    BOARD[2][0] = 3
    if check_square(3, 0, 2):
        print("FAILURE")
    if check_square(5, 0, 7):
        print("SUCCESS")
    print_board()


if __name__ == '__main__':
    main()
