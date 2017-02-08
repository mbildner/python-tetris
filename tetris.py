from tetromino import Tetromino
from random import randrange
from copy import deepcopy
import os

class Tetris(object):   
    def __init__(self):
        board = []
        for y in range(20):
            row = []
            for x in range(10):
                row.append(0)
            board.append(row)

        self.board = board
        self.piece = self.get_random_piece()

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

        self.piece = self.get_random_piece()


    def get_random_piece(self):
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


    def up(self):
        return self.__move_piece__('up')
    
    def left(self):
        return self.__move_piece__('left')

    def right(self):
        return self.__move_piece__('right')

    def down(self):
        self.__move_piece__('down')

    def __move_piece__(self, direction):
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
            raise "not a valid command"

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
                        self.freeze_current_piece()
                        return False

        self.piece.x, self.piece.y = x, y

        return True


game = Tetris()

while True:
    print game.print_board()
    next_move = raw_input("> ")
    
    if next_move:
        game.__move_piece__(next_move)

    game.__move_piece__('down')
    os.system('clear')


