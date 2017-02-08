from tetromino import Tetromino
from random import randrange
from time import sleep
from copy import deepcopy
import json
import os

class Tetris(object):   
    def __init__(self):
        self.board = self.empty_board()
        self.piece = self.random_piece()
        self.lines_scored = []
        self.is_running = True

    def empty_board(self):
        board = []
        for y in range(20):
            row = []
            for x in range(10):
                row.append(0)
            board.append(row)

        return board

    def print_board(self):
        piece_indices = []
        for row_i, row in enumerate(self.piece.rotations[self.piece.current]):
            for col_i, col in enumerate(row):
                if col == 1:
                    piece_indices.append((col_i + self.piece.x, row_i + self.piece.y))

        board = ""
        for row_i, row in enumerate(self.board):
            board += "\n"
            for col_i, col in enumerate(row):
                n = 0
                if (col_i, row_i) in piece_indices:
                    n += 1

                board += str(col + n)
                board += " "

        return board

    def freeze_current_piece(self):
        for row_i, row in enumerate(self.piece.rotations[self.piece.current]):
            for col_i, col in enumerate(row):
                if col == 1:
                    self.board[row_i + self.piece.y][col_i + self.piece.x] = 1

        lines_cleared = 0
        for row_i, row in enumerate(self.board):
            if all(col == 1 for col in row):
                lines_cleared += 1
                self.board.pop()
                self.board.insert(0, [0 for _ in range(10)])


        if lines_cleared:
            self.lines_scored.append(lines_cleared)

        self.piece = self.random_piece()


    def random_piece(self):
        p = randrange(0, 7)

        if p == 0:
          return Tetromino.T()
        elif p == 1:
          return Tetromino.J()
        elif p == 2:
          return Tetromino.L()
        elif p == 3:
          return Tetromino.Z()
        elif p == 4:
          return Tetromino.S()
        elif p == 5:
          return Tetromino.Block()
        elif p == 6:
          return Tetromino.Line()

    def rotate_piece(self):
        new_current = (self.piece.current + 1) % len(self.piece.rotations)

        x, y = self.piece.x, self.piece.y

        for row_i, row in enumerate(self.piece.rotations[new_current]):
            for col_i, col in enumerate(row):
                if col == 1:
                    if row_i + y >= len(self.board):
                        return False

                    if col_i + x < 0:
                        return False

                    if col_i + x >= len(self.board[0]):
                        return False


        for row_i, row in enumerate(self.piece.rotations[new_current]):
            for col_i, col in enumerate(row):
                if col == 1:

                    if row_i >= len(self.board) - 1:
                        return False

                    if self.board[row_i + y][col_i + x] == 1:
                        return False

        self.piece.current = new_current

        return True

    def end_game(self):
        score = sum(self.lines_scored)

        self.is_running = False
        self.board = self.empty_board()
        self.piece = self.random_piece()
        self.lines_scored = []


    def move_piece(self, direction):
        x, y = self.piece.x, self.piece.y

        if direction == 'up':
            self.rotate_piece()
        elif direction == 'left':
            x -= 1
        elif direction == 'right':
            x += 1
        elif direction == 'down':
            y += 1
        else:
            raise Exception(direction + " is not a valid command")

        for row_i, row in enumerate(self.piece.rotations[self.piece.current]):
            for col_i, col in enumerate(row):
                if col == 1:
                    if row_i + y >= len(self.board):
                        self.freeze_current_piece()
                        return False

                    if col_i + x < 0:
                        return False

                    if col_i + x >= len(self.board[0]):
                        return False


        for row_i, row in enumerate(self.piece.rotations[self.piece.current]):
            for col_i, col in enumerate(row):
                if col == 1:

                    if row_i >= len(self.board) - 1:
                        return False


                    if self.board[row_i + y][col_i + x] == 1:
                        if self.piece.y == 0:
                            self.end_game()
                        else:
                            self.freeze_current_piece()
                        return False

        self.piece.x, self.piece.y = x, y

        return True


if __name__ == "__main__":
    scores = []
    game = Tetris()

    moves = [
            'left',
            'down',
            'down',
            'down',
            'down',
            'down',
            'down',
            'down',
            'down',
            'down',
            'right',
            'down',
            'down',
            'down',
            'down',
            'down',
            'down',
            'down',
            'down',
            'down',
            'right',
            'right',
            'right',
            'down',
            'down',
            'down',
            'down',
            'down',
            'down',
            'down',
            'down',
            'down',
            'right',
            'right',
            'right',
            'right',
            'right',
            'down',
            'down',
            'down',
            'down',
            'down',
            'down',
            'down',
            'right',
            'right',
            'right',
            'right',
            'right',
            'right',
            'right',
            'right',
            'right',
            'right',
            'right',
            'right',
    ]

    scores = []

    for _ in range(100):
        for move in moves:
            print game.print_board()
            print sum(game.lines_scored)
            sleep(0.01)

            next_move = move

            if next_move:
                game.move_piece(next_move)

            game.move_piece('down')
            os.system('clear')

