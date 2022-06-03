import pygame
from .constants import *
from .piece import *

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.green_pieces = self.red_pieces = 10
        self.create_board()

    def draw_nodes(self, win):
        win.fill(WHITE)
        pygame.draw.rect(win, GREEN, (12*SQUARE_SIZE, 0, SQUARE_SIZE, SQUARE_SIZE))
        i = 0
        while (i < 3):
            pygame.draw.rect(win, GREEN, ((i+11)*SQUARE_SIZE, 1*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            i = i+2
        i = 0
        while (i < 5):
            pygame.draw.rect(win, GREEN, ((i+10)*SQUARE_SIZE, 2*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            i = i+2
        i = 0
        while (i < 7):
            pygame.draw.rect(win, GREEN, ((i+9)*SQUARE_SIZE, 3*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            i = i+2
        i = 0
        while (i < 25):
            color = YELLOW
            if(i>7 and i<18):
                color = GREY
            pygame.draw.rect(win, color, (i*SQUARE_SIZE, 4*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            i = i+2
        i = 0
        while (i < 23):
            color = YELLOW
            if(i>5 and i<17):
                color = GREY
            pygame.draw.rect(win, color, ((i+1)*SQUARE_SIZE, 5*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            i = i+2
        i = 0
        while (i < 21):
            color = YELLOW
            if(i>3 and i<17):
                color = GREY
            pygame.draw.rect(win, color, ((i+2)*SQUARE_SIZE, 6*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            i = i+2
        i = 0
        while (i < 19):
            color = YELLOW
            if(i>1 and i<17):
                color = GREY
            pygame.draw.rect(win, color, ((i+3)*SQUARE_SIZE, 7*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            i = i+2
        i = 0
        while (i < 17):
            color = YELLOW
            if(i>3 and i<22):
                color = GREY
            pygame.draw.rect(win, GREY, ((i+4)*SQUARE_SIZE, 8*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            i = i+2
        i = 0
        while (i < 19):
            color = YELLOW
            if(i>1 and i<17):
                color = GREY
            pygame.draw.rect(win, color, ((i+3)*SQUARE_SIZE, 9*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            i = i+2
        i = 0
        while (i < 21):
            color = YELLOW
            if(i>3 and i<17):
                color = GREY
            pygame.draw.rect(win, color, ((i+2)*SQUARE_SIZE, 10*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            i = i+2
        i = 0
        while (i < 23):
            color = YELLOW
            if(i>5 and i<17):
                color = GREY
            pygame.draw.rect(win, color, ((i+1)*SQUARE_SIZE, 11*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            i = i+2
        i = 0
        while (i < 25):
            color = YELLOW
            if(i>7 and i<18):
                color = GREY
            pygame.draw.rect(win, color, (i*SQUARE_SIZE, 12*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            i = i+2
        i = 0
        while (i < 7):
            pygame.draw.rect(win, BLUE, ((i+9)*SQUARE_SIZE, 13*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            i = i+2
        i = 0
        while (i < 5):
            pygame.draw.rect(win, BLUE, ((i+10)*SQUARE_SIZE, 14*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            i = i+2
        i = 0
        while (i < 3):
            pygame.draw.rect(win, BLUE, ((i+11)*SQUARE_SIZE, 15*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            i = i+2
        pygame.draw.rect(win, BLUE, (12*SQUARE_SIZE, 16*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
    def create_board(self):
        self.board.append([]) #row 0
        i = 0
        while(i<12):
            self.board[0].append(-1)
            i = i + 1
        self.board[0].append(Piece(0, 12, PIECE_GREEN))
        i = 0
        while(i<12):
            self.board[0].append(-1)
            i = i + 1


        while(i<11):
            self.board[1].append(-1)
            i = i + 1
        i = 0
        self.board.append([])
        while (i < 3):
            if(i%2==0):
                self.board[1].append(Piece(1, i+11, PIECE_GREEN))
            else:
                self.board[1].append(-1)     
            i = i + 1
        while(i<11):
            self.board[1].append(-1)
            i = i + 1
        
        
        while(i<10):
            self.board[2].append(-1)
            i = i + 1
        i = 0
        self.board.append([])
        while (i < 5):
            if(i%2==0):
                self.board[2].append(Piece(2, i+10, PIECE_GREEN))
            else:
                self.board[2].append(-1)     
            i = i+1
        while(i<10):
            self.board[2].append(-1)
            i = i + 1


        while(i<9):
            self.board[3].append(-1)
            i = i + 1
        i = 0
        self.board.append([])
        while (i < 7):
            if(i%2==0):
                self.board[3].append(Piece(3, i+9, PIECE_GREEN))
            else:
                self.board[3].append(-1)
            i = i+1
        while(i<9):
            self.board[3].append(-1)
            i = i + 1
        
        
        i = 0
        self.board.append([])
        while (i<24):
            if(i%2==0):
                if(i>6 and i<18):
                    self.board[4].append(1)
                else:
                    self.board[4].append(0)
            else:
                self.board[4].append(-1)
            i = i + 1
            
         
        i = 0
        self.board.append([])
        while (i<24):
            if(i%2==1):
                if(i>5 and i<19):
                    self.board[5].append(1)
                else:
                    self.board[5].append(0)
            else:
                self.board[5].append(-1)
            i = i + 1


        i = 0
        self.board.append([])
        while (i<24):
            if(i%2==0):
                if(i<2 or i>22):
                    self.board[6].append(-1)
                if(i>4 and i<20):
                    self.board[6].append(1)
                else:
                    self.board[6].append(0)
            else:
                self.board[6].append(-1)
            i = i + 1

        
        i = 0
        self.board.append([])
        while (i<24):
            if(i%2==1):
                if(i<3 or i>21):
                    self.board[7].append(-1)
                if(i>3 and i<19):
                    self.board[7].append(1)
                else:
                    self.board[7].append(0)
            else:
                self.board[7].append(-1)
            i = i + 1

        i = 0
        self.board.append([])
        while (i < 24):
            if(i%2==0):
                if(i<4 or i>20):
                   self.board[8].append(-1)
                else:
                    self.board[8].append(1)
            else:
                self.board[8].append(-1)
            i = i + 1

        i = 0
        self.board.append([])
        while (i<24):
            if(i%2==1):
                if(i<3 or i>21):
                    self.board[9].append(-1)
                if(i>3 and i<19):
                    self.board[9].append(1)
                else:
                    self.board[9].append(0)
            else:
                self.board[9].append(-1)
            i = i + 1

        i = 0
        self.board.append([])
        while (i<24):
            if(i%2==0):
                if(i<2 or i>22):
                    self.board[10].append(-1)
                if(i>4 and i<20):
                    self.board[10].append(1)
                else:
                    self.board[10].append(0)
            else:
                self.board[10].append(-1)
            i = i + 1

        i = 0
        self.board.append([])
        while (i<24):
            if(i%2==1):
                if(i>5 and i<19):
                    self.board[11].append(1)
                else:
                    self.board[11].append(0)
            else:
                self.board[11].append(-1)
            i = i + 1

        i = 0
        self.board.append([])
        while (i<24):
            if(i%2==0):
                if(i>6 and i<18):
                    self.board[12].append(1)
                else:
                    self.board[12].append(0)
            else:
                self.board[12].append(-1)
            i = i + 1
        
        
        while(i<9):
            self.board[13].append(-1)
            i = i + 1
        i = 0
        self.board.append([])
        while (i < 7):
            if(i%2==0):
                self.board[13].append(Piece(13, i+9, PIECE_BLUE))
            else:
                self.board[13].append(-1)
            i = i+1
        while(i<9):
            self.board[13].append(-1)
            i = i + 1

        while(i<10):
            self.board[14].append(-1)
            i = i + 1
        i = 0
        self.board.append([])
        while (i < 5):
            if(i%2==0):
                self.board[14].append(Piece(14, i+10, PIECE_BLUE))
            else:
                self.board[14].append(-1)     
            i = i+1
        while(i<10):
            self.board[14].append(-1)
            i = i + 1

        while(i<11):
            self.board[15].append(-1)
            i = i + 1
        i = 0
        self.board.append([])
        while (i < 3):
            if(i%2==0):
                self.board[15].append(Piece(15, i+11, PIECE_BLUE))
            else:
                self.board[15].append(-1)     
            i = i+1
        while(i<11):
            self.board[15].append(-1)
            i = i + 1

        
        self.board.append([])
        i = 0
        while(i<12):
            self.board[16].append(-1)
            i = i + 1
        self.board[16].append(Piece(16, 12, PIECE_BLUE))
        i = 0
        while(i<12):
            self.board[16].append(-1)
            i = i + 1

    def draw(self, win):
        self.draw_nodes(win)
        i = j = 0
        while i < 17:
            print(i)
            while j < 25:
                print(j)
                piece=self.board[i][j]
                if piece != 0 or 1 or -1:
                    piece.draw(win)
                j = j + 1
            i = i + 1
        
        