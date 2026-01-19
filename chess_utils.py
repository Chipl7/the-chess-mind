from typing import Any


def print_board(
        board,
        borders: bool = True,
        invert_color: bool = False,
        empty_square: str = "⭘") -> Any:
    return board.unicode(
        borders=borders,
        invert_color=invert_color,
        empty_square=empty_square)
