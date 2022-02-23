BLACK = 1
WHITE = 0


def removeIslands(matrix):
    if not matrix:
        return

    if not all(len(row) == len(matrix[0]) for row in matrix):
        return

    visited = [[False] * len(matrix[0]) for _ in matrix]
    for i, row in enumerate(matrix):
        for j, v in enumerate(row):
            if (i, j) not in visited:
                _remove_island(i, j, matrix, visited)

    return matrix


def _remove_island(start_i: int, start_j: int, matrix: list, visited: list):
    island = []
    stk = [(start_i, start_j)]
    hit_edge = False
    while stk:
        i, j = stk.pop()
        if matrix[i][j] == WHITE or visited[i][j]:
            continue

        visited[i][j] = True
        if _is_edge(matrix, i, j):
            hit_edge = True

        if not hit_edge:
            island.append((i, j))

        stk.extend(_get_neighbors(matrix, i, j))

    if not hit_edge:
        for i, j in island:
            matrix[i][j] = WHITE


def _is_edge(matrix, i, j) -> bool:
    return i == 0 or j == 0 or i == len(matrix) - 1 or j == len(matrix[0]) - 1


from typing import List, Tuple


def _get_neighbors(matrix, i, j) -> List[Tuple[int, int]]:
    nbrs = []
    if i > 0:
        nbrs.append((i - 1, j))
    if j > 0:
        nbrs.append((i, j - 1))
    if i < len(matrix) - 1:
        nbrs.append((i + 1, j))
    if j < len(matrix[0]) - 1:
        nbrs.append((i, j + 1))

    return nbrs
