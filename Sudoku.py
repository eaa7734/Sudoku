"""
Author: Edgar Argueta
Filename: Sudoku.py
"""

rows = 9
cols = 9
BOARD = [[0 for i in range(rows)] for j in range(cols)]

def printBoard():
    for x in range(rows):
        for y in range(cols):
            print(BOARD[x][y], end=' ')
        print()

printBoard()