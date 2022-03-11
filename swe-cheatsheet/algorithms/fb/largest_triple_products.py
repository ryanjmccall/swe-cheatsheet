import math
import heapq
from functools import reduce


def findMaxProduct(arr):
    if len(arr) <= 2:
        return [-1] * len(arr)

    products = [1] * len(arr)
    products[0] = products[1] = -1
    maxes = []
    heapq.heappush(maxes, arr[0])
    heapq.heappush(maxes, arr[1])
    func = lambda x, y: x * y
    for i, val in enumerate(arr[2:], start=2):
        heapq.heappush(maxes, val)
        products[i] = reduce(func, heapq.nlargest(3, maxes))

    return products


print(findMaxProduct([1, 2, 3, 4, 5]))
print(findMaxProduct([2, 4, 7, 1, 5, 3]))
