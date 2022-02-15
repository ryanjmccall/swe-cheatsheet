from collections import Counter


def h_index(citations: list) -> int:
    max_cites = len(citations)
    counts = Counter((min(x, max_cites) for x in citations))

    total = 0
    for n in range(max_cites, -1, -1):
        total += counts[n]
        if total >= n:
            return n

    return 0


print(h_index([3, 5, 0, 1, 3]))
