"""
Author: Edgar Argueta
Filename: SudokuGUI.py
"""

import copy
import pygame
from Sudoku import *
ROWS = 9
COLS = 9

GRAY = (224,224,224)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


def setupBoard(gameDisplay, board, error):
    """
    Setups up the view of a board and makes all of the
    squares.
    """
    num_font = pygame.font.SysFont("Helvetica", 50)
    for i in range(ROWS):
        for j in range(COLS):
            if board[j][i] != '.':
                num = board[j][i]
                num_text = num_font.render(str(num), True, BLACK)
                rect = num_text.get_rect(center=(40, 40)).move(i*80, j*80)
                gameDisplay.blit(num_text, rect)
    error_text = num_font.render("Errors left: " + str(error), True, BLACK)
    error_rect = error_text.get_rect(center=(40, 40)).move(800, 300)
    gameDisplay.blit(error_text, error_rect)

    pygame.draw.line(gameDisplay, GRAY, (0, 80), (720, 80), 2)
    pygame.draw.line(gameDisplay, GRAY, (0, 160), (720, 160), 2)
    pygame.draw.line(gameDisplay, GRAY, (0, 320), (720, 320), 2)
    pygame.draw.line(gameDisplay, GRAY, (0, 400), (720, 400), 2)
    pygame.draw.line(gameDisplay, GRAY, (0, 560), (720, 560), 2)
    pygame.draw.line(gameDisplay, GRAY, (0, 640), (720, 640), 2)

    pygame.draw.line(gameDisplay, GRAY, (80, 0), (80, 720), 2)
    pygame.draw.line(gameDisplay, GRAY, (160, 0), (160, 720), 2)
    pygame.draw.line(gameDisplay, GRAY, (320, 0), (320, 720), 2)
    pygame.draw.line(gameDisplay, GRAY, (400, 0), (400, 720), 2)
    pygame.draw.line(gameDisplay, GRAY, (560, 0), (560, 720), 2)
    pygame.draw.line(gameDisplay, GRAY, (640, 0), (640, 720), 2)

    pygame.draw.line(gameDisplay, BLACK, (240, 0), (240, 720), 2)
    pygame.draw.line(gameDisplay, BLACK, (480, 0), (480, 720), 2)
    pygame.draw.line(gameDisplay, BLACK, (720, 0), (720, 720), 2)
    pygame.draw.line(gameDisplay, BLACK, (0, 240), (720, 240), 2)
    pygame.draw.line(gameDisplay, BLACK, (0, 480), (720, 480), 2)


def gameOver(gameDisplay):
    """
    This is the game over screen when a
    player loses
    """
    font = pygame.font.SysFont("Helvetica", 180)
    start_font = pygame.font.SysFont("Helvetica", 50)
    text = font.render("You Lose", True, RED)
    rect = text.get_rect(center=(90, 90)).move((450, 250))
    gameDisplay.blit(text, rect)
    start_text = start_font.render("New game?", True, BLACK, WHITE)
    start_rect = start_text.get_rect(center=(40, 40)).move(500, 400)
    gameDisplay.blit(start_text, start_rect)


def gameWon(gameDisplay):
    """
    This is the game won screen when a
    player wins.
    """
    font = pygame.font.SysFont("Helvetica", 180)
    start_font = pygame.font.SysFont("Helvetica", 50)
    text = font.render("You Won", True, GREEN)
    rect = text.get_rect(center=(90, 90)).move((450, 250))
    gameDisplay.blit(text, rect)
    start_text = start_font.render("New game?", True, BLACK, WHITE)
    start_rect = start_text.get_rect(center=(40, 40)).move(500, 400)
    gameDisplay.blit(start_text, start_rect)


def newGame(mode):
    """
    This setups a new game of sudoku
    """
    if mode == 1:
        mode = EASY_MODE
    elif mode == 2:
        mode = INTERMEDIATE_MODE
    elif mode == 3:
        mode = HARD_MODE
    else:
        mode = EXPERT_MODE
    board = [['.' for i in range(ROWS)] for j in range(COLS)]
    solve_sudoku(board)
    solved_board = copy.deepcopy(board)
    print_board(solved_board)
    create_sudoku(board, mode)
    return board, solved_board


def selectMode(gameDisplay):
    """
    The start screen for the user to pick a
    difficulty for the sudoku game.
    """
    question_font = pygame.font.SysFont("Helvetica", 80)
    quest = question_font.render("Pick a difficulty", True, BLACK)
    quest_rect = quest.get_rect(center=(80, 80)).move(350, 200)
    gameDisplay.blit(quest, quest_rect)

    font = pygame.font.SysFont("Helvetica", 50)
    easy = font.render("Easy = 1", True, BLACK)
    easy_rect = easy.get_rect(center=(25, 25)).move(75, 350)
    gameDisplay.blit(easy, easy_rect)

    inter = font.render("Intermediate = 2", True, BLACK)
    inter_rect = inter.get_rect(center=(25, 25)).move(300, 350)
    gameDisplay.blit(inter, inter_rect)

    hard = font.render("Hard = 3", True, BLACK)
    hard_rect = hard.get_rect(center=(25, 25)).move(550, 350)
    gameDisplay.blit(hard, hard_rect)

    expert = font.render("Expert = 4", True, BLACK)
    expert_rect = expert.get_rect(center=(25, 25)).move(750, 350)
    gameDisplay.blit(expert, expert_rect)


def main():
    """
    Main functions that handles the actual game running,
    startup, and end.
    """
    pygame.init()
    gameDisplay = pygame.display.set_mode((950, 720))
    gameDisplay.fill(WHITE)
    clock = pygame.time.Clock()
    board = None
    solved_board = None
    errors = 5
    gameStart = True
    crashed = False
    gameDone = False
    while not crashed:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            col = pos[0] // 80
            row = pos[1] // 80
            if gameStart:
                selectMode(gameDisplay)
                if event.type == pygame.KEYDOWN and 49 <= event.key <= 52:
                    num = event.key-48
                    board, solved_board = newGame(num)
                    gameDisplay.fill(WHITE)
                    setupBoard(gameDisplay, board, errors)
                    gameStart = False
                    gameDone = False
            if gameDone:
                if event.type == pygame.MOUSEBUTTONDOWN and 440 <= pos[0] <= 640 and 420 <= pos[1] <= 460:
                    gameDisplay.fill(WHITE)
                    errors = 5
                    gameStart = True
            if event.type == pygame.QUIT:
                crashed = True
            else:
                if event.type == pygame.KEYDOWN and row <= 8 and col <= 8:
                    num = event.key-48
                    if board[row][col] == '.':
                        if solved_board[row][col] == num:
                            board[row][col] = num
                            gameDisplay.fill(WHITE)
                            if not find_empty(board):
                                gameWon(gameDisplay)
                                gameDone = True
                            else:
                                setupBoard(gameDisplay, board, errors)
                        else:
                            errors -= 1
                            if errors == 0:
                                gameDisplay.fill(BLACK)
                                gameOver(gameDisplay)
                                gameDone = True
                            else:
                                gameDisplay.fill(WHITE)
                                setupBoard(gameDisplay, board, errors)

            print(event)

        pygame.display.update()
        clock.tick(60)
    pygame.quit()

main()


