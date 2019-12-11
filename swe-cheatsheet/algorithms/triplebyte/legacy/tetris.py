
# Tetris
# Grid
# driver steps the game through
# test loss
# test 'tetris'
# test stuck
# rotate
# piece structures
#
from random import random


class Tetris(object):

    def __init__(self):
        self.width = 10
        self.height = 50
        self.grid = self._new_grid()
        self._piece = None
        self._piece_rotation = 0
        self._piece_i = None
        self._piece_j = None
        self.pieces = [
            [   # square, only 1 shape
                [
                    ['X', 'X'],
                    ['X', 'X']
                ]
            ],
            [   # L, 4 shapes
                [
                    [' ', ' ', ' '],
                    ['X', 'X', 'X'],
                    ['X', ' ', ' ']
                ],
                [
                    ['X', 'X', ' '],
                    [' ', 'X', ' '],
                    [' ', 'X', ' ']
                ],
                [
                    [' ', ' ', 'X'],
                    ['X', 'X', 'X'],
                    [' ', ' ', ' ']
                ],
                [
                    [' ', 'X', ' '],
                    [' ', 'X', ' '],
                    [' ', 'X', 'X']
                ]
            ]
        ]

    def _new_grid(self):
        return [[' '] * self.width for _ in range(self.height)]

    def step(self, move: str):
        if not self._piece:
            self._piece = int(random() * len(self.pieces))

        if move == 'rot':
            self.rotate(move)
        elif move == 'l':
            pass
        elif move == 'r':
            pass
        elif move == 'd':
            pass
        else:
            self.advance_down()

    def rotate(self, move: str):
        if self.apply_rotate_move(test=True):
            self.apply_rotate_move(test=False)

    def apply_rotate_move(self, test: bool):
        # loop over next_shape and only render if doesn't go oob or touches existing blocks
        next_shape = self.pieces[self._piece][self._piece_rotation]

        for i in range(len(next_shape)):
            for j in range(len(next_shape[0])):
                if next_shape[i][j] != ' ':
                    rend_i = i + self._piece_i
                    rend_j = j + self._piece_j
                    if self.grid[rend_i][rend_j] != ' ':  # touches existing cell
                        return False
                    if rend_i < 0 or rend_i > self.width - 1:
                        return False
                    if rend_j < 0 or rend_j > self.height - 1:
                        return False

        return True


def drive():
    tetris = Tetris()
    while True:
        move = input()
        result = tetris.step(move)
        if not result:
            break

drive()
