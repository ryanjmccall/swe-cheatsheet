
class BoardError(Exception):
    pass


_EMPTY = '-'


class Board:
    def __init__(self):
        size = 3
        self.matrix = []
        self.moves = 0
        self.total_moves = size * size
        for _ in range(size):
            self.matrix.append([_EMPTY] * size)

    def _add_token(self, token: str, i: int, j: int) -> bool:
        if self.matrix[i][j] == _EMPTY:
            self.matrix[i][j] = token
            self.moves += 1
            return True
        return False

    def print(self):
        for row in self.matrix:
            print('|'.join(row))

    def _is_full(self) -> bool:
        return self.moves >= self.total_moves

    def _ai_move(self):
        for i, row in enumerate(self.matrix):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] == _EMPTY:
                    self._add_token(token='O', i=i, j=j)
                    return

        raise BoardError('')

    def run_game(self):
        while not self._is_full():
            self._human_move()
            self.print()

            if not self._is_full():
                self._ai_move()
                self.print()


    def _human_move(self):
        while True:
            raw = input('enter move: ')
            splits  = raw.split(' ')
            if len(splits) != 2:
                continue
            try:
                i = int(splits[0])
                j = int(splits[1])
            except ValueError:
                continue

            if i < 0 or j < 0 or i >= len(self.matrix) or j >= len(self.matrix[0]):
                continue

            added = self._add_token('X', i, j)
            if not added:
                continue

            break

    def _has_won(self, human: bool) -> bool:
        sym = 'X' if human else 'O'
        for row in self.matrix:
            if all(i == sym for i in row):
                return True

def test():
    b = Board()
    b.run_game()

test()
