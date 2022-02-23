

def minimumPassesOfMatrix(m):
    q = [(i, j) for i, row in enumerate(m) for j, v in enumerate(row) if v > 0]
    if not q:
        return -1

    passes = 0
    while q:
        nxt = []
        for i, j in q:
            for r, c in get_cardinal_adjacent(i, j, m):
                if m[r][c] < 0:
                    m[r][c] *= -1
                    nxt.append((r, c))

        q = nxt
        passes += 1

    return passes-1 if all_positive(m) else -1


def all_positive(m):
    return all(v >= 0 for r in m for v in r)


def get_cardinal_adjacent(i, j, m):
    nbrs = []
    if i > 0:
        nbrs.append((i - 1, j))
    if j > 0:
        nbrs.append((i, j - 1))
    if i < len(m) - 1:
        nbrs.append((i + 1, j))
    if j < len(m[0]) - 1:
        nbrs.append((i, j + 1))
    return nbrs


print(minimumPassesOfMatrix(
    [
    [1, 0, 0, -2, -3],
    [-4, -5, -6, -2, -1],
    [0, 0, 0, 0, -1],
    [-1, 0, 3, 0, 3]
  ]
))
