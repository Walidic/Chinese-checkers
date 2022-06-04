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

    def winner(self):
        if self.checkBlue():
            return PIECE_BLUE
        elif self.checkGreen():
            return PIECE_GREEN
        return None

    def checkBlue(self):
        nodes = [
            (0, 12),
            (1, 11),
            (1, 13),
            (2, 10),
            (2, 12),
            (2, 14),
            (3, 9),
            (3, 11),
            (3, 13),
            (3, 15),
        ]
        for node in nodes:
            piece = Piece(node[0], node[1], PIECE_BLUE)
            if self.board.get_piece(node[0], node[1]) == piece:
                pass
            else:
                return False
        return True

    def checkGreen(self):
        nodes = [
            (16, 12),
            (15, 11),
            (15, 13),
            (14, 10),
            (14, 12),
            (14, 14),
            (13, 9),
            (13, 11),
            (13, 13),
            (13, 15),
        ]
        for node in nodes:
            piece = Piece(node[0], node[1], PIECE_GREEN)
            if self.board.get_piece(node[0], node[1]) == piece:
                pass
            else:
                return False
        return True

    def draw_valid_moves(self, moves):
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
