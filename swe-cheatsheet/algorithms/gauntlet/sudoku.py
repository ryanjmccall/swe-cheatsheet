from typing import Iterable


class Sudoku(object):
    def __init__(self):
        self.size = 9
        self.board = [[0] * self.size for _ in range(self.size)]

    def __str__(self) -> str:
        return '\n'.join(' '.join(str(v) for v in row) for row in self.board) + '\n'

    def solve(self) -> bool:
        return self._solve(0, 0)

    def _solve(self, i, j):
        for val in range(1, self.size + 1):
            self.board[i][j] = val
            if self._is_valid(i, j):
                if i == j == self.size - 1:
                    return True

                elif j < self.size - 1:
                    if self._solve(i, j + 1):
                        return True
                else:
                    if self._solve(i + 1, 0):
                        return True

        self.board[i][j] = 0
        return False

    def _is_valid(self, i, j) -> True:
        if not self._is_complete_group(self.board[i]):
            return False
        if not self._is_complete_group((row[j] for row in self.board)):
            return False

        row_start = i // 3
        col_start = j // 3
        square = []
        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                square.append(self.board[row][col])
        if not self._is_complete_group(square):
            return False
        return True

    def _is_complete_group(self, values: Iterable[int]) -> bool:
        seen = set()
        has_empty = False
        for v in values:
            if v:
                if v in seen:
                    return False
                else:
                    seen.add(v)
            else:
                has_empty = True

        return True if has_empty else len(seen) == 9


def test():
    game = Sudoku()
    print(str(game))
    if game.solve():
        print(str(game))
    else:
        print('impossible')


test()
