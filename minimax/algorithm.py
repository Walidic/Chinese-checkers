from copy import deepcopy
import pygame

from Game.board import Board
from Game.constants import PIECE_BLUE, PIECE_GREEN 
GREEN =(0,128,0)
BLUE = (0,0,255)

def minimax(position,depth,max_player,game):
    if depth == 0 or position.winner() !=None:
        return position.evaluate() , position
    
    if max_player:
        maxEval = float('-inf')
        best_move =  None
        for move in get_all_moves(position,PIECE_GREEN,game):
            evaluation = minimax(move,depth-1,False,game)[0]
            maxEval = max(maxEval,evaluation)
            if maxEval == evaluation:
                best_move = move
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move =  None
        for move in get_all_moves(position,PIECE_BLUE,game):
            evaluation = minimax(move,depth-1,True,game)[0]
            minEval = min(minEval,evaluation)
            if minEval == evaluation:
                best_move = move
        return minEval, best_move

def simulate_move(piece,move,board,game):
    if len(move) == 0 :
        return board
    board.move(piece,move[0][0],move[0][1])
    return board

def get_all_moves(board,color,game):
    moves = []
    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move in valid_moves:
            if len(move) == 0 :
                continue
            temp_board = deepcopy(board)
            temp_piece =temp_board.get_piece(piece.row,piece.col)
            new_board = simulate_move(temp_piece,move,temp_board,game)
            moves.append(new_board)
    return moves