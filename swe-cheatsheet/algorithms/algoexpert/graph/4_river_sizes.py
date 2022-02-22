from typing import List

RIVER = 1
LAND = 0


def riverSizes(matrix: List[List[int]]) -> List[int]:
    sizes = []
    for i, r in enumerate(matrix):
        for j, v in enumerate(r):
            bfs_river_size(matrix, i, j, sizes)

    return sizes


def bfs_river_size(m, i, j, sizes):
    size = 0
    q = [(i, j)]
    for r, c in q:
        if m[r][c] != RIVER:
            continue

        m[r][c] = LAND
        size += 1
        if r > 0:
            q.append((r - 1, c))
        if r < len(m) - 1:
            q.append((r + 1, c))
        if c > 0:
            q.append((r, c - 1))
        if c < len(m[0]) - 1:
            q.append((r, c + 1))

    if size:
        sizes.append(size)

