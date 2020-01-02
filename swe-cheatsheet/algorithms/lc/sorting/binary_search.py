from typing import Optional, List


def binary_search(a: List[int], val: int) -> Optional[int]:
    left = 0
    right = len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        v = a[mid]
        if v < val:
            left = mid + 1
        elif v > val:
            right = mid - 1
        else:
            return mid
    return None


def t():
    a = [0, 1, 2, 3, 5, 7, 9, 11]
    for i, v in enumerate(a):
        assert binary_search(a, v) == i
    assert binary_search(a, 77) is None
    assert binary_search(a, -77) is None


t()
