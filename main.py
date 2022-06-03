import pygame
from Game.constants import *
from Game.board import *
from Game.piece import *

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chinese Checkers')

def main():
    run = True
    clock = pygame.time.Clock()

    while  run:
        clock.tick(FPS)
        board = Board()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        board.draw(WIN)
        pygame.display.update()
    pygame.quit()

main()