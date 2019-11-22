from typing import List


class WordSearch(object):
    def __init__(self, grid: List[List[str]]):
        self.grid = grid

    def find_word(self, w: str) -> (int, int):
        for i in range(len(self.grid)):
            if self._check_right(i, w):
                return True

        for i in range(len(self.grid[0])):
            if self._check_down(i, w):
                return True

        return False

    def _check_right(self, index, w: str) -> bool:
        for j in range(len(self.grid[index])):
            if w[j] != self.grid[index][j]:
                return False
        return True

    def _check_down(self, index, w: str) -> bool:
        for i in range(len(self.grid)):
            if w[i] != self.grid[i][index]:
                return False
        return True


ws = WordSearch([
    ['c', 'a', 't'],
    ['a', 's', 'p'],
    ['r', 's', 'z'],
])
print(ws.find_word('car'))
print(ws.find_word('cat'))
# for word, expected in [
#     # ('cat', (0, 0)),
#     # ('car', (0, 0)),
#     ('sz', (2, 1)),
#     ('pz', (1, 2)),
#     ('z', (2, 2)),
#     ('cats', (-1, -1)),
#     ('cars', (-1, -1)),
#     ('zz', (-1, -1)),
#
# ]:
#     actual = ws.find_word(word)
#     assert actual == expected, (word, actual, expected)
