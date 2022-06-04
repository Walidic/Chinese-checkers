import pygame
from Game.constants import *
from Game.board import *
from Game.piece import *
from Game.engine import *
from minimax.algorithm import minimax
FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chinese Checkers")


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():
    run = True
    clock = pygame.time.Clock()
    game = engine(WIN)

    while run:
        clock.tick(FPS)
        if game.turn == PIECE_GREEN:
            value,new_board = minimax(game.board,3,PIECE_GREEN,game) # the higher the depth the better the ai , change the depth to change the difficulty
            game.ai_move()

        if game.winner() != None:
            print(game.winner())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                if game.turn == PIECE_BLUE:
                    game.select(row, col)

        game.update()
    pygame.quit()


main()
