import chess
from chess_utils import print_board
from chess_game import illegal_moves


def main():
    board = chess.Board()
    print(print_board(board))

if __name__ == "__main__":
    main()
