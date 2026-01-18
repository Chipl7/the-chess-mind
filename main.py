import chess

board = chess.Board()

print(board)

move = chess.Move.from_uci("e2e4")
board.push(move)

print(board)
