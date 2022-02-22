import heapq


def add(num, min_heap, max_heap):
    if len(min_heap) + len(max_heap) <= 1:
        heapq.heappush(max_heap, -num)
        return

    median = get_median(min_heap, max_heap)
    if num > median:
        heapq.heappush(min_heap, num)
    else:
        heapq.heappush(max_heap, -num)


def get_median(minh, maxh):
    if len(minh) > len(maxh):
        return minh[0]
    elif len(minh) < len(maxh):
        return -maxh[0]
    return (minh[0] - maxh[0]) / 2.0


def rebalance(min_heap, max_heap):
    if len(min_heap) > len(max_heap) + 1:
        root = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -root)
    elif len(max_heap) > len(min_heap) + 1:
        root = heapq.heappop(max_heap)
        heapq.heappush(min_heap, -root)


def running_median(a):
    min_heap, max_heap = [], []
    res = []
    for n in a:
        add(n, min_heap, max_heap)
        rebalance(min_heap, max_heap)
        res.append(get_median(min_heap, max_heap))
    return res


print(running_median([2, 1, 4, 7, 2, 0, 5]))
# 2, 1.5, 2, 3, 2, 2, 2

