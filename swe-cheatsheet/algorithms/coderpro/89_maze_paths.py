
from typing import List


def maze_paths(m: List[List[int]]):
    p = [[0] * len(m[0]) for _ in range(len(m))]
    p[0][0] = 1
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 0:
                if i > 0:
                    p[i][j] += p[i-1][j]
                if j > 0:
                    p[i][j] += p[i][j-1]

    return p[-1][-1]


print(maze_paths([
    [0, 1, 0],
    [0, 0, 1],
    [0, 0, 0]
]))

