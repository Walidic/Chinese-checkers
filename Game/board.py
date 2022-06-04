from cmath import pi
import pygame

from .constants import *

from .piece import *


class Board:
    def __init__(self):
        self.board = []
        self.green_pieces = self.red_pieces = 10
        self.create_board()

    def draw_nodes(self, win):

        win.fill(WHITE)

        pygame.draw.rect(win, GREEN, (12 * SQUARE_SIZE, 0, SQUARE_SIZE, SQUARE_SIZE))

        i = 0

        while i < 3:

            pygame.draw.rect(
                win,
                GREEN,
                ((i + 11) * SQUARE_SIZE, 1 * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
            )

            i = i + 2

        i = 0

        while i < 5:

            pygame.draw.rect(
                win,
                GREEN,
                ((i + 10) * SQUARE_SIZE, 2 * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
            )

            i = i + 2

        i = 0

        while i < 7:

            pygame.draw.rect(
                win,
                GREEN,
                ((i + 9) * SQUARE_SIZE, 3 * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
            )

            i = i + 2

        i = 0

        while i < 25:

            color = YELLOW

            if i > 7 and i < 18:

                color = GREY

            pygame.draw.rect(
                win, color, (i * SQUARE_SIZE, 4 * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            )

            i = i + 2

        i = 0

        while i < 23:

            color = YELLOW

            if i > 5 and i < 17:

                color = GREY

            pygame.draw.rect(
                win,
                color,
                ((i + 1) * SQUARE_SIZE, 5 * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
            )

            i = i + 2

        i = 0

        while i < 21:

            color = YELLOW

            if i > 3 and i < 17:

                color = GREY

            pygame.draw.rect(
                win,
                color,
                ((i + 2) * SQUARE_SIZE, 6 * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
            )

            i = i + 2

        i = 0

        while i < 19:

            color = YELLOW

            if i > 1 and i < 17:

                color = GREY

            pygame.draw.rect(
                win,
                color,
                ((i + 3) * SQUARE_SIZE, 7 * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
            )

            i = i + 2

        i = 0

        while i < 17:

            color = YELLOW

            if i > 3 and i < 22:

                color = GREY

            pygame.draw.rect(
                win,
                GREY,
                ((i + 4) * SQUARE_SIZE, 8 * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
            )

            i = i + 2

        i = 0

        while i < 19:

            color = YELLOW

            if i > 1 and i < 17:

                color = GREY

            pygame.draw.rect(
                win,
                color,
                ((i + 3) * SQUARE_SIZE, 9 * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
            )

            i = i + 2

        i = 0

        while i < 21:

            color = YELLOW

            if i > 3 and i < 17:

                color = GREY

            pygame.draw.rect(
                win,
                color,
                ((i + 2) * SQUARE_SIZE, 10 * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
            )

            i = i + 2

        i = 0

        while i < 23:

            color = YELLOW

            if i > 5 and i < 17:

                color = GREY

            pygame.draw.rect(
                win,
                color,
                ((i + 1) * SQUARE_SIZE, 11 * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
            )

            i = i + 2

        i = 0

        while i < 25:

            color = YELLOW

            if i > 7 and i < 18:

                color = GREY

            pygame.draw.rect(
                win,
                color,
                (i * SQUARE_SIZE, 12 * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
            )

            i = i + 2

        i = 0

        while i < 7:

            pygame.draw.rect(
                win,
                BLUE,
                ((i + 9) * SQUARE_SIZE, 13 * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
            )

            i = i + 2

        i = 0

        while i < 5:

            pygame.draw.rect(
                win,
                BLUE,
                ((i + 10) * SQUARE_SIZE, 14 * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
            )

            i = i + 2

        i = 0

        while i < 3:

            pygame.draw.rect(
                win,
                BLUE,
                ((i + 11) * SQUARE_SIZE, 15 * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
            )

            i = i + 2

        pygame.draw.rect(
            win, BLUE, (12 * SQUARE_SIZE, 16 * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
        )

    def create_board(self):

        self.board.append([])  # row 0

        i = 0

        while i < 12:

            self.board[0].append(-1)

            i = i + 1

        self.board[0].append(Piece(0, 12, (152, 255, 152)))

        i = 0

        while i < 12:

            self.board[0].append(-1)

            i = i + 1

        self.board.append([])  # row 1

        i = 0

        while i < 11:

            self.board[1].append(-1)

            i = i + 1

        i = 0

        while i < 3:

            if i % 2 == 0:

                self.board[1].append(Piece(1, i + 11, (152, 255, 152)))

            else:

                self.board[1].append(-1)

            i = i + 1

        i = 0

        while i < 11:

            self.board[1].append(-1)

            i = i + 1

        self.board.append([])  # row 2

        i = 0

        while i < 10:

            self.board[2].append(-1)

            i = i + 1

        i = 0

        while i < 5:

            if i % 2 == 0:

                self.board[2].append(Piece(2, i + 10, (152, 255, 152)))

            else:

                self.board[2].append(-1)

            i = i + 1

        i = 0

        while i < 10:

            self.board[2].append(-1)

            i = i + 1

        self.board.append([])  # row 3

        i = 0

        while i < 9:

            self.board[3].append(-1)

            i = i + 1

        i = 0

        while i < 7:

            if i % 2 == 0:

                self.board[3].append(Piece(3, i + 9, (152, 255, 152)))

            else:

                self.board[3].append(-1)

            i = i + 1

        i = 0

        while i < 9:

            self.board[3].append(-1)

            i = i + 1

        self.board.append([])  # row 4

        i = 0

        while i < 24:

            if i % 2 == 0:

                if i > 6 and i < 18:

                    self.board[4].append(1)

                else:

                    self.board[4].append(0)

            else:

                self.board[4].append(-1)

            i = i + 1

        self.board.append([])  # row 5

        i = 0

        while i < 24:

            if i % 2 == 1:

                if i > 5 and i < 19:

                    self.board[5].append(1)

                else:

                    self.board[5].append(0)

            else:

                self.board[5].append(-1)

            i = i + 1

        self.board.append([])  # row 6

        i = 0

        while i < 24:

            if i % 2 == 0:

                if i < 2 or i > 22:

                    self.board[6].append(-1)

                if i > 4 and i < 20:

                    self.board[6].append(1)

                else:

                    self.board[6].append(0)

            else:

                self.board[6].append(-1)

            i = i + 1

        self.board.append([])  # row 7

        i = 0

        while i < 24:

            if i % 2 == 1:

                if i < 3 or i > 21:

                    self.board[7].append(-1)

                if i > 3 and i < 19:

                    self.board[7].append(1)

                else:

                    self.board[7].append(0)

            else:

                self.board[7].append(-1)

            i = i + 1

        self.board.append([])  # row 8

        i = 0

        while i < 24:

            if i % 2 == 0:

                if i < 4 or i > 20:

                    self.board[8].append(-1)

                else:

                    self.board[8].append(1)

            else:

                self.board[8].append(-1)

            i = i + 1

        self.board.append([])  # row 9

        i = 0

        while i < 24:

            if i % 2 == 1:

                if i < 3 or i > 21:

                    self.board[9].append(-1)

                if i > 3 and i < 19:

                    self.board[9].append(1)

                else:

                    self.board[9].append(0)

            else:

                self.board[9].append(-1)

            i = i + 1

        self.board.append([])  # row 10

        i = 0

        while i < 24:

            if i % 2 == 0:

                if i < 2 or i > 22:

                    self.board[10].append(-1)

                if i > 4 and i < 20:

                    self.board[10].append(1)

                else:

                    self.board[10].append(0)

            else:

                self.board[10].append(-1)

            i = i + 1

        self.board.append([])  # row 11

        i = 0

        while i < 24:

            if i % 2 == 1:

                if i > 5 and i < 19:

                    self.board[11].append(1)

                else:

                    self.board[11].append(0)

            else:

                self.board[11].append(-1)

            i = i + 1

        self.board.append([])  # row 12

        i = 0

        while i < 24:

            if i % 2 == 0:

                if i > 6 and i < 18:

                    self.board[12].append(1)

                else:

                    self.board[12].append(0)

            else:

                self.board[12].append(-1)

            i = i + 1

        self.board.append([])  # row 13

        i = 0

        while i < 9:

            self.board[13].append(-1)

            i = i + 1

        i = 0

        while i < 7:

            if i % 2 == 0:

                self.board[13].append(Piece(13, i + 9, PIECE_BLUE))

            else:

                self.board[13].append(-1)

            i = i + 1

        i = 0

        while i < 9:

            self.board[13].append(-1)

            i = i + 1

        self.board.append([])  # row 14

        i = 0

        while i < 10:

            self.board[14].append(-1)

            i = i + 1

        i = 0

        while i < 5:

            if i % 2 == 0:

                self.board[14].append(Piece(14, i + 10, PIECE_BLUE))

            else:

                self.board[14].append(-1)

            i = i + 1

        i = 0

        while i < 10:

            self.board[14].append(-1)

            i = i + 1

        self.board.append([])  # row 15

        i = 0

        while i < 11:

            self.board[15].append(-1)

            i = i + 1

        i = 0

        while i < 3:

            if i % 2 == 0:

                self.board[15].append(Piece(15, i + 11, PIECE_BLUE))

            else:

                self.board[15].append(-1)

            i = i + 1

        i = 0

        while i < 11:

            self.board[15].append(-1)

            i = i + 1

        self.board.append([])  # row 16

        i = 0

        while i < 12:

            self.board[16].append(-1)

            i = i + 1

        self.board[16].append(Piece(16, 12, PIECE_BLUE))

        i = 0

        while i < 12:

            self.board[16].append(-1)

            i = i + 1

    def draw(self, win):
        self.draw_nodes(win)
        for row in range(ROWS):
            for col in range(COLS - 1):
                piece = self.board[row][col]
                if piece != 0:
                    if piece != -1:
                        if piece != 1:
                            piece.draw(win)

    def move(self, piece, row, col):

        self.board[piece.row][piece.col], self.board[row][col] = (
            self.board[row][col],
            self.board[piece.row][piece.col],
        )

        piece.move(row, col)

    def get_piece(self, row, col):
        if row>15 or col>24:
            return None
        return self.board[row][col]

    def get_valid_moves(self, piece):

        moves = []

        left = (piece.row, piece.col - 2)

        right = (piece.row, piece.col + 2)

        topLeft = (piece.row - 1, piece.col - 1)

        topRight = (piece.row - 1, piece.col + 1)

        bottomLeft = (piece.row + 1, piece.col - 1)

        bottomRight = (piece.row + 1, piece.col + 1)

        moves.append(self._traverse_left(piece, left))

        moves.append(self._traverse_right(piece, right))

        moves.append(self._traverse_top_left(piece, topLeft))

        moves.append(self._traverse_top_right(piece, topRight))

        moves.append(self._traverse_bottom_left(piece, bottomLeft))

        moves.append(self._traverse_bottom_right(piece, bottomRight))

        # for move in moves:

        #     if len(move) != 0:

        #         x = move[0][0]

        #         y = move[0][1]

        #         if self._check_jump(x, y) in moves:

        #             pass

        #         else:

        #             moves.append(self._check_jump(x, y))

        i = 0

        for move in moves:

            if len(move) != 0:

                x = move[0][0]

                y = move[0][1]

                if self.get_piece(x, y) == 0 or -1:

                    moves[i] = []

        return moves

    def _traverse_left(self, piece, left):

        moves = []

        if self.get_piece(left[0], left[1]) == 1:

            coord = (left[0], left[1])

            moves.append(coord)

        return moves

    def _traverse_right(self, piece, right):

        moves = []

        if self.get_piece(right[0], right[1]) == 1:

            coord = (right[0], right[1])

            moves.append(coord)

        return moves

    def _traverse_top_left(self, piece, topLeft):

        moves = []

        if self.get_piece(topLeft[0], topLeft[1]) == 1:

            coord = (topLeft[0], topLeft[1])

            moves.append(coord)

        return moves

    def _traverse_top_right(self, piece, topRight):

        moves = []

        if self.get_piece(topRight[0], topRight[1]) == 1:

            coord = (topRight[0], topRight[1])

            moves.append(coord)

        return moves

    def _traverse_bottom_left(self, piece, bottomLeft):

        moves = []

        if self.get_piece(bottomLeft[0], bottomLeft[1]) == 1:

            coord = (bottomLeft[0], bottomLeft[1])

            moves.append(coord)

        return moves

    def _traverse_bottom_right(self, piece, bottomRight):

        moves = []

        if self.get_piece(bottomRight[0], bottomRight[1]) == 1:

            coord = (bottomRight[0], bottomRight[1])

            moves.append(coord)

        return moves

    def _check_jump(self, row, col):

        jumps = []

        if row < 3 or row > 13:

            return jumps

        if col < 3 or col > 21:

            return jumps

        left = (row, col - 2)

        right = (row, col + 2)

        topLeft = (row - 1, col - 1)

        topRight = (row - 1, col + 1)

        bottomLeft = (row + 1, col - 1)

        bottomRight = (row + 1, col + 1)

        if self.get_piece(left[0], left[1]) != 0 and 1 and -1:

            if self.get_piece(left[0], left[1] - 2) == 1 or 0:

                coords = (left[0], left[1] + 2)

                jumps.append(coords)

        if self.get_piece(right[0], right[1]) != 0 and 1 and -1:

            if self.get_piece(right[0], right[1] + 2) == 1 or 0:

                coords = (right[0], right[1] + 2)

                jumps.append(coords)

        if self.get_piece(topLeft[0], topLeft[1]) != 0 and 1 and -1:

            if self.get_piece(topLeft[0] - 1, topLeft[1] - 1) == 1 or 0:

                coords = (topLeft[0] - 1, topLeft[1] - 1)

                jumps.append(coords)

        if self.get_piece(topRight[0], topRight[1]) != 0 and 1 and -1:

            if self.get_piece(topRight[0] - 1, topRight[1] + 1) == 1 or 0:

                coords = (topRight[0] - 1, topRight[1] + 1)

                jumps.append(coords)

        if self.get_piece(bottomLeft[0], bottomLeft[1]) != 0 and 1 and -1:

            if self.get_piece(bottomLeft[0] + 1, bottomLeft[1] - 1) == 1 or 0:

                coords = (bottomLeft[0] + 1, bottomLeft[1] - 1)

                jumps.append(coords)

        if self.get_piece(bottomRight[0], bottomRight[1]) != 0 and 1 and -1:

            if self.get_piece(bottomRight[0] + 1, bottomRight[1] + 1) == 1 or 0:

                coords = (bottomRight[0] + 1, bottomRight[1] + 1)

                jumps.append(coords)

        return jumps

    def get_all_pieces(self,color):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece !=0 :
                    if piece != 1:
                        if piece != -1:
                            if piece.color == color:
                                pieces.append(piece)
        return pieces

    def get_board(self):
        return self.board



    def evaluate(self):
        score = 0
        for row in self.board:
            for piece in row:
                if piece == 0 or 1 or -1:
                    return 0
                if piece.color == PIECE_GREEN:
                    score = score + piece.row
                else:
                    score = score - (16 -piece.row) # 16 is the top of the blue triangle
        return score

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
            if self.get_piece(node[0], node[1]) == piece:
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
            if self.get_piece(node[0], node[1]) == piece:
                pass
            else:
                return False
        return True