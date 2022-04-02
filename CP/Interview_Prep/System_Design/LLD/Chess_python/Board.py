from .Piece import Piece, PieceFactory
from .Move import ChessPosition, MoveCommand
from .constants import CHESS_BOARD_SIZE, INITIAL_PIECE_SET_SINGE

class Board:
    def __init__(self):
        self._board = [[0]*()]
