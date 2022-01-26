import math


class Sudoku(object):
    EMPTY = 0

    def __init__(self, board):
        for row in board:
            assert len(row) == len(board)
        self.board = board
        self.puzzle_dim = len(board)
        self._box_dim = int(math.sqrt(self.puzzle_dim))

    def __repr__(self) -> str:
        return '\n'.join(' '.join(str(v) for v in row) for row in self.board) + '\n'

    def solve(self):
        i, j = self.find_empty()
        if i == -1:
            return False

        for val in range(1, self.puzzle_dim + 1):
            if self.valid(i, j, val):
                self.board[i][j] = val

                if self.solve():
                    return True

                self.board[i][j] = self.EMPTY

        return False

    def valid(self, i, j, val) -> bool:
        return (self._valid_row(i, j, val)
                and self._valid_col(i, j, val)
                and self._valid_box(i, j, val))

    def _valid_row(self, i, j, val):
        for k in range(len(self.board[0])):
            if self.board[i][k] == val and j != k:
                return False
        return True

    def _valid_col(self, i, j, val):
        for k in range(len(self.board)):
            if self.board[k][j] == val and i != k:
                return False
        return True

    def _valid_box(self, i, j, val):
        start_i = (i // self._box_dim) * self._box_dim
        start_j = (j // self._box_dim) * self._box_dim
        for r in range(start_i, start_i + self._box_dim):
            for c in range(start_j, start_j + self._box_dim):
                if self.board[r][c] == val and (i, j) != (r, c):
                    return False
        return True

    def find_empty(self) -> (int, int):
        for i, row in enumerate(self.board):
            for j, val in enumerate(row):
                if val == self.EMPTY:
                    return i, j
        return -1, -1


def test():
    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    sudo = Sudoku(board)
    print(sudo)
    sudo.solve()
    print(sudo)


test()
