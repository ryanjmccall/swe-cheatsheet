_DELTAS = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def minimumHours(rows, columns, grid):
    min_dist = [[float('inf')] * columns for _ in range(rows)]
    stk = []
    for i, row in enumerate(grid):
        for j, v in enumerate(row):
            if v == 1:
                stk.append((i, j, 0))

    while stk:
        new_stk = []
        for i, j, dist in stk:
            if dist < min_dist[i][j]:
                min_dist[i][j] = dist
                for dy, dx in _DELTAS:
                    new_i = i + dy
                    new_j = j + dx
                    if 0 <= new_i < rows and 0 <= new_j < columns:
                        new_stk.append((new_i, new_j, dist + 1))

        stk = new_stk

    max_dist = 0
    for row in min_dist:
        max_dist = max(max_dist, max(row))

    return max_dist


def t():
    grid = [
        [1,0,0,0,0],
        [0,1,0,0,0],
        [0,0,1,0,0],
        [0,0,0,1,0],
        [0,0,0,0,1]
    ]

    print(minimumHours(5, 5, grid))

t()
