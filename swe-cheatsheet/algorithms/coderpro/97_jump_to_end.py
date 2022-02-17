from typing import List


def min_hops_backward(a: List[int]) -> int:
    hops = [float('inf')] * len(a)
    hops[-1] = 0
    for i in range(len(a) - 2, -1, -1):
        remain = min(len(a) - 1 - i, a[i])
        for dist in range(remain, 0, -1):
            right = min(i + dist, len(a) - 1)
            hops[i] = min(hops[i], hops[right] + 1)

    return hops[0]


def min_hops(a):
    hops = [float('inf')] * len(a)
    hops[0] = 0
    for i, v in enumerate(a):
        for hop in range(1, v + 1):
            right = i + hop
            if right >= len(a):
                break
            hops[right] = min(hops[right], hops[i] + 1)

    return hops[-1]


print(min_hops_backward(a=[3, 2, 5, 1, 1, 9, 3, 4]))
print(min_hops(a=[3, 2, 5, 1, 1, 9, 3, 4]))
