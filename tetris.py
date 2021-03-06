from tetromino import Tetromino
from time import sleep
import os
import sys
from random import randrange
import copy

from board_printer import BoardPrinter
from action_report import ActionReport

from itertools import cycle

import numpy as np

class Tetris(object):
    def __init__(self, number_of_rows=16, number_of_cols=10, printer=BoardPrinter(number_of_cols=10)):
        self.number_of_rows = number_of_rows
        self.number_of_cols = number_of_cols
        self.printer = printer
        self.start()

    def start(self):
        self.board = self.empty_board()
        self.piece = self.random_piece()
        self.lines_scored = []
        self.total_lines = 0
        self.moves = 0
        self.is_running = True


    def save(self):
        number_of_rows = self.number_of_rows
        number_of_cols = self.number_of_cols
        piece = self.piece.clone()
        board = copy.deepcopy(self.board)
        lines_scored = copy.deepcopy(self.lines_scored)
        moves = self.moves
        total_lines = self.total_lines
        is_running = self.is_running

        game = Tetris(number_of_rows, number_of_cols)
        game.piece = piece
        game.board = board
        game.lines_scored = lines_scored
        game.moves = moves
        game.total_lines = total_lines
        game.is_running = is_running

        return game

    def empty_board(self):
        return np.zeros([self.number_of_rows, self.number_of_cols])

    def combine_game_state(self):
        piece_indices = []
        for row_i, row in enumerate(self.piece.rotations[self.piece.current]):
            for col_i, col in enumerate(row):
                if col == 1:
                    piece_indices.append((col_i + self.piece.x, row_i + self.piece.y))

        combined_state=[]
        for row_i, row in enumerate(self.board):
            combined_row = []
            for col_i, col in enumerate(row):
                if (col_i, row_i) in piece_indices:
                    combined_row.append(1)
                else:
                    combined_row.append(col)

            combined_state.append(combined_row)

        return combined_state

    def print_board(self):
        return self.printer.print_game_state(self.combine_game_state())

    def freeze_current_piece(self):
        for row_i, row in enumerate(self.piece.rotations[self.piece.current]):
            for col_i, col in enumerate(row):
                if col == 1:
                    self.board[row_i + self.piece.y][col_i + self.piece.x] = 1

        lines_cleared = 0
        for row_i, row in enumerate(self.board):
            if all(col != 0 for col in row):
                lines_cleared += 1
                self.board = np.append(
                        [[0 for _ in range(10)]],
                        self.board[:-1],
                        axis=0
                        )

        if lines_cleared:
            self.total_lines += lines_cleared
            self.lines_scored.append(lines_cleared)

        self.piece = self.random_piece()

        return lines_cleared

    def trapped_space(self):
        total_empty = 0

        rotated = np.rot90(self.board)

        for column in rotated:
            first_full = np.where(column > 0)[0]

            if first_full.size > 0:
                empties = column[np.where(column[first_full[0]:] == 0)]
                total_empty += len(empties)

        return total_empty

    def random_piece(self):
        return Tetromino.random(
                y=0,
                x=randrange(0, self.number_of_cols - 2)
                )

    def rotate_piece(self, kick_offset=0):
        new_current = (self.piece.current + 1) % len(self.piece.rotations)

        x, y = self.piece.x + kick_offset, self.piece.y

        for row_i, row in enumerate(self.piece.rotations[new_current]):
            for col_i, col in enumerate(row):
                if col == 1:
                    if row_i + y >= len(self.board):
                        return False

                    if col_i + x < 0:
                        return False

                    if col_i + x >= len(self.board[0]):
                        return self.rotate_piece(kick_offset=kick_offset - 1)


        for row_i, row in enumerate(self.piece.rotations[new_current]):
            for col_i, col in enumerate(row):
                if col == 1:

                    if row_i >= len(self.board) - 1:
                        return False

                    if self.board[row_i + y][col_i + x] == 1:
                        return False

        self.piece.x, self.piece.y = x, y
        self.piece.current = new_current

        return True

    def hard_drop(self):
        if not self.is_running:
            raise Exception("You must start a game before you can move")

        original_piece = self.piece
        moves_stack = [self.move_piece('down')]
        while self.piece is original_piece:
            moves_stack.append(self.move_piece('down'))

        return moves_stack[-1]

    def move_piece(self, direction):
        if not self.is_running:
            raise Exception("You must start a game before you can move")

        x, y = self.piece.x, self.piece.y

        if direction == 'up':
            self.rotate_piece()
        elif direction == 'left':
            x -= 1
        elif direction == 'right':
            x += 1
        elif direction == 'down':
            y += 1
        elif direction == 'drop':
            return self.hard_drop()

        else:
            raise Exception(direction + " is not a valid command")

        for row_i, row in enumerate(self.piece.rotations[self.piece.current]):
            for col_i, col in enumerate(row):
                if col == 1:
                    if row_i + y >= len(self.board):
                        score_from_freeze = self.freeze_current_piece()
                        self.moves += 1
                        return ActionReport(state=self.combine_game_state(), done=False, score=self.total_lines, score_from_action=score_from_freeze, did_perform_move=False)

                    if col_i + x < 0:
                        self.moves += 1
                        return ActionReport(state=self.combine_game_state(), done=False, score=self.total_lines, score_from_action=0, did_perform_move=False)

                    if col_i + x >= len(self.board[0]):
                        self.moves += 1
                        return ActionReport(state=self.combine_game_state(), done=False, score=self.total_lines, score_from_action=0, did_perform_move=False)


        for row_i, row in enumerate(self.piece.rotations[self.piece.current]):
            for col_i, col in enumerate(row):
                if col == 1:
                    if row_i >= len(self.board) - 1:
                        self.moves += 1
                        return ActionReport(state=self.combine_game_state(), piece=self.piece, done=False, score=self.total_lines, score_from_action=0, did_perform_move=False)

                    if self.board[row_i + y][col_i + x] != 0:
                        if self.piece.y == 0:
                            self.is_running = False
                            self.moves += 1
                            return ActionReport(state=self.combine_game_state(), done=True, score=self.total_lines, score_from_action=0, did_perform_move=False)
                        elif direction == 'down':
                            score_from_freeze = self.freeze_current_piece()
                            self.moves += 1
                            return ActionReport(state=self.combine_game_state(), done=False, score=self.total_lines, score_from_action=score_from_freeze, did_perform_move=True)
                        else:
                            self.moves += 1
                            return ActionReport(state=self.combine_game_state(), done=False, score=self.total_lines, score_from_action=0, did_perform_move=True)


        self.piece.x, self.piece.y = x, y

        self.moves += 1
        return ActionReport(state=self.combine_game_state(), done=False, score=self.total_lines, score_from_action=0, did_perform_move=True)

steps_til_drop_gen = cycle(reversed(range(4)))
def step_forward(game, next_move):
    ''' keep track of number of moves to drop'''
    steps_till_drop = next(steps_til_drop_gen)
    report = game.move_piece(next_move)
    if report.done:
        return report
    elif steps_till_drop == 0: #automatic drop
        new_report = game.move_piece('down')
        if new_report.done:
            return new_report

    return report

if __name__ == "__main__":
    scores = []
    game = Tetris()

    moves = [
            'left', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'right', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'right', 'right', 'right', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'right', 'right', 'right', 'right', 'right', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right',
    ]
    for _ in range(50000):
        for move in moves:
            print(game.print_board())
            print(str.format("\n\n\nlines: {0}", game.total_lines))
            sleep(0.05)

            next_move = move
            if next_move:
                report = game.move_piece(next_move)
                if report.done:
                    game.start()

            report = game.move_piece('down')
            if report.done:
                game.start()

            os.system('clear')
    sys.exit(0)

