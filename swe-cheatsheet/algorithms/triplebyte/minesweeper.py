"""
board with mines
visible board
blank areas
- could do bfs to find all such cells
click types
- explore
- flag
cell object
- is_mine
- is_flagged
- is_explored
- mine_count
- is_empty

program loop
- input loop
- receive i, j location click and click type
- update board and respond accordingly
"""
from random import random


class Cell:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.mine = False
        self.flagged = False
        self.explored = False
        self.mine_count = 0

    def is_empty(self) -> bool:
        return self.mine_count == 0

    def is_hit(self):
        return self.mine and self.explored

    def __str__(self):
        if self.explored:
            if self.mine:
                return '*'
            else:
                return str(self.mine_count) if self.mine_count else ' '

        elif self.flagged:
            return '1'

        return '?'


class Game:
    def __init__(self):
        self.h = 10
        self.w = 10
        self.cells = []
        self.cell_count = self.h * self.w
        self.moves = 0
        self._hit_mine = False
        for i in range(self.h):
            self.cells.append([Cell(i, j) for j in range(self.w)])
        self._add_mines(10)
        self._update_mine_counts()

    def _add_mines(self, num: int):
        if num > self.cell_count:
            raise ValueError('..')

        n = 0
        while n < num:
            i = int(random() * len(self.cells))
            j = int(random() * len(self.cells))
            if not self.cells[i][j].mine:
                self.cells[i][j].mine = True
                n += 1

    def _update_mine_counts(self):
        for i, row in enumerate(self.cells):
            for j, c in enumerate(row):
                for y, x in self._get_valid_neighbors(i, j):
                    if self.cells[y][j + x].mine:
                        c.mine_count += 1

    def _get_valid_neighbors(self, i, j):
        nbrs = []
        for y, x in [
            (-1, -1), (-1, 0), (-1, 1),
            (1, -1), (1, 0), (1, 1),
            (0, -1), (0, 1)
        ]:
            if self._in_bounds(i + y, j + x):
                nbrs.append((i + y, j + x))
        return nbrs

    def _in_bounds(self, i, j):
        return 0 <= i < self.h and 0 <= j < self.w

    def is_finished(self) -> bool:
        return self._hit_mine or self.moves == self.cell_count

    def close(self):
        print('lose' if self._hit_mine else 'win')

    def make_move(self, i, j):
        cell = self.cells[i][j]
        if cell.explored:
            print('already explored')
            return

        self.moves += 1
        cell.explored = True

        if cell.mine:
            self._hit_mine = True

        if cell.is_empty():
            self._dfs(cell)

    def _dfs(self, cell):
        pass # TODO uncover all cells reachable from cell that have no neighboring mines

    def render_game(self):
        for row in self.cells:
            print('|'.join(str(c) for c in row))

    @classmethod
    def parse_move(cls):
        while True:
            print('enter move (i, j) or "quit"')
            raw = input()
            if raw.lower() == 'quit':
                return -1, -1
            else:
                splits = raw.split(' ')
                if len(splits) != 2:
                    print('bad input')
                    continue
                # catch errors
                return int(splits[0]), int(splits[1])


def run():
    g = Game()
    while True:
        g.render_game()
        if g.is_finished():
            g.close()
            g = Game()

        i, j = Game.parse_move()
        if i == -1:
            break

        g.make_move(i, j)


run()
