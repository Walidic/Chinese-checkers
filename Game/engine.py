import pygame
from .constants import *
from .board import *


class engine:
    def __init__(self, win):
        self.selected = None
        self.board = Board()
        self.turn = PIECE_BLUE
        self.valid_moves = []
        self.win = win

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def reset():
        self.selected = None
        self.board = Board()
        self.turn = PIECE_BLUE
        self.valid_moves = {}

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece != -1:
            if piece != 0:
                if piece != 1 and piece.color == self.turn:
                    self.selected = piece
                    self.valid_moves = self.board.get_valid_moves(piece)
                    return True
        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        coord = (row, col)
        if self.selected and piece == 1 and coord in self.valid_moves:
            self.board.move(self.selected, row, col)
            self.change_turn()
        else:
            return False

        return True

    def draw_valid_moves(self, moves):
        print(moves)
        for move in moves:
            if len(move) != 0:
                row = move[0][0]
                col = move[0][1]
                pygame.draw.circle(
                    self.win,
                    RED,
                    (
                        ((col) * SQUARE_SIZE) + (SQUARE_SIZE // 2),
                        ((row) * SQUARE_SIZE) + (SQUARE_SIZE // 2),
                    ),
                    6,
                )

    def change_turn(self):
        self.valid_moves = []
        if self.turn == PIECE_BLUE:
            self.turn = PIECE_GREEN
        else:
            self.turn = PIECE_BLUE
