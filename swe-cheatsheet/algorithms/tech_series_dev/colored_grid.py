from typing import Tuple, List


class Solution(object):

    _NEIGHBOR_DELTAS = (
        (0, -1),
        (0, 1),
        (-1, 0),
        (1, 0),
    )

    def __init__(self, grid):
        self._grid = grid

    def get_max_connected_size(self) -> int:
        max_size = 0
        for i in range(len(self._grid)):
            for j in range(len(self._grid[i])):
                size = self._connected_size_for(i, j)
                max_size = max(max_size, size)

        return max_size

    def _connected_size_for(self, i: int, j: int) -> int:
        size = 0
        color = self._grid[i][j]
        visited = set()
        stack = [(i, j)]
        while stack:
            cur_i, cur_j = stack.pop()
            if (cur_i, cur_j) in visited:
                continue

            if self._grid[cur_i][cur_j] != color:
                continue

            # add cell i, j to contiguous component
            visited.add((cur_i, cur_j))
            size += 1

            # extend frontier
            stack.extend(self._get_neighbors(cur_i, cur_j))

        return size

    def _get_neighbors(self, i: int, j: int) -> List[Tuple]:
        coords = []
        for d_i, d_j in self._NEIGHBOR_DELTAS:
            n_i = i + d_i
            n_j = j + d_j
            row_in_bounds = 0 <= n_i < len(self._grid)
            col_in_bounds = 0 <= n_j < len(self._grid[0])
            if row_in_bounds and col_in_bounds:
                coords.append((n_i, n_j))

        return coords


def main():
    grid = [
        ['r', 'g', 'b'],
        ['r', 'r', 'r'],
        ['g', 'g', 'r']
    ]
    print(Solution(grid).get_max_connected_size())


main()
