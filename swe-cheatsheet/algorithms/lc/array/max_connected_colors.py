from typing import Tuple, Iterable


class Grid(object):
    def __init__(self, g):
        self.grid = g
        self.height = len(g)
        self.width = len(g[0])
        self._deltas = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def max_connected_colors_iter(self) -> int:
        visited = set()
        max_val = 0
        for i in range(self.height):
            for j in range(self.width):
                if (i, j) not in visited:
                    # max_val = max(max_val, self._count_connected_iter(i, j, visited))
                    max_val = max(max_val, self._count_connected_recur(i, j, visited))
        return max_val

    def _count_connected_iter(self, i, j, visited: set) -> int:
        count = 0
        color = self.grid[i][j]
        stk = [(i, j)]  # invariant: stk maintains unvisited, in-bounds positions of the same color
        while stk:
            a, b = stk.pop()
            count += 1
            visited.add((a, b))
            stk.extend(self._valid_neighbors(a, b, visited, color))
        return count

    def _count_connected_recur(self, i, j, visited: set) -> int:
        color = self.grid[i][j]

        def dfs(a, b) -> int:
            count = 1
            visited.add((a, b))
            for x, y in self._valid_neighbors(a, b, visited, color):
                count += dfs(x, y)
            return count

        return dfs(i, j)

    def _valid_neighbors(self, a: int, b: int, visited: set, color) -> Iterable[Tuple[int, int]]:
        for dy, dx in self._deltas:
            y = a + dy
            x = b + dx
            if 0 <= y < self.height and 0 <= x < self.width:
                if (y, x) not in visited:
                    if self.grid[y][x] == color:
                        yield y, x


def test():
    grid = [[4, 3, 3, 1],
            [4, 1, 1, 1],
            [1, 1, 0, 2]]

    print(Grid(grid).max_connected_colors_iter())

test()