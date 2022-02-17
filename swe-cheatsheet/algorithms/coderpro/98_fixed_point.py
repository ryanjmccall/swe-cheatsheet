from typing import List


def fixed_point(a: List[int]) -> int:
    left, right = 0, len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] < mid:
            left = mid + 1
        elif a[mid] > mid:
            right = mid - 1
        else:
            return mid

    return -1


def mean(a: list):
    avg = 0
    for i, v in enumerate(a):
        avg += (v - avg) / (i + 1)

    return avg


print(fixed_point([-5, 1, 3, 4]))
