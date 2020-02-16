"""
Author: Edgar Argueta
Filename: Sudoku.py
"""
import random

ROWS = 9
COLS = 9
EASY_MODE = 38
INTERMEDIATE_MODE = 30
HARD_MODE = 24
EXPERT_MODE = 17
EMPTY = [0] * 2


def print_board(board):
    print()
    for x in range(ROWS):
        print("\t", end='')
        for y in range(COLS):
            print(board[x][y], end=' ')
        print()


def check_row(board, num, row, col):
    for y in range(COLS):
        if y != col:
            if board[row][y] == num:
                return False
    return True


def check_col(board, num, row, col):
    for x in range(ROWS):
        if x != row:
            if board[x][col] == num:
                return False
    return True


def check_square(board, num, row, col):
    start_x = row - (row % 3)
    start_y = col - (col % 3)
    for x in range(start_x,start_x+3):
        for y in range(start_y, start_y+3):
            if x != row and y != col:
                if board[x][y] == num:
                    return False
    return True


def check_all(board, num, row, col):
    if check_row(board, num, row, col) and check_col(board, num, row, col) and check_square(board, num, row, col):
        return True
    return False


def create_sudoku(board, mode):
    count = 81 - mode
    while count != 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if board[row][col] == '.':
            continue
        board[row][col] = '.'
        count -= 1


def find_empty(board):
    for x in range(ROWS):
        for y in range(COLS):
            if board[x][y] == '.':
                EMPTY[0] = x
                EMPTY[1] = y
                return True
    return False


def solve_sudoku(board):
    if not find_empty(board):
        return True

    else:
        temp_row = EMPTY[0]
        temp_col = EMPTY[1]
        numbers = [1,2,3,4,5,6,7,8,9]
        for x in range(1, ROWS+1):
            num = random.choice(numbers)
            numbers.remove(num)
            if check_all(board, num, temp_row, temp_col):
                board[temp_row][temp_col] = num
                if solve_sudoku(board):
                    return True
                board[temp_row][temp_col] = '.'
        return False


def main():
    board = [['.' for i in range (ROWS)] for j in range(COLS)]
    solve_sudoku(board)
    print_board(board)
    create_sudoku(board, EASY_MODE)
    print_board(board)
    if solve_sudoku(board):
        print_board(board)


if __name__ == '__main__':
    main()
