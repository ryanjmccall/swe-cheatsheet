from heapq import *
from typing import Optional


def kth_largest(arr, k):
    return sorted(arr)[-k]


def kth_largest_heap(arr, k):
    return nlargest(k, arr)[-1]


def quickselect(arr, k):
    k = len(arr) - k
    left = 0
    right = len(arr) - 1
    while left <= right:
        index = partition(arr, left, right)
        if index > k:
            right = index - 1
        elif index < k:
            left = index + 1
        else:
            return arr[index]
    return -1


def partition(arr, left, right):
    pivot = arr[right]
    i = left
    for j in range(left, right):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[right] = arr[right], arr[i]
    return i


print(kth_largest(arr=[8,7,2,3,4,1,5,6,9,0], k=3))
print(kth_largest_heap(arr=[8,7,2,3,4,1,5,6,9,0], k=3))
print(quickselect(arr=[8,7,2,3,4,1,5,6,9,0], k=3))


def quickselect(arr: list, k: int) -> Optional[int]:
    """return the kth largest element from a list in linear time"""
    k = len(arr) - k
    l = 0
    r = len(arr) - 1
    while l <= r:
        pivot = _partition(arr, l, r)
        if pivot < k:
            l += 1
        elif pivot > k:
            r -= 1
        else:
            return arr[pivot]

    return None


def _partition(arr: list, l: int, r: int) -> int:
    pivot = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[r] = arr[r], arr[i]
    return i
