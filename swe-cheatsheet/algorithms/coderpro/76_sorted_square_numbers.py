from typing import List, Iterable


def sorted_square_num(a: List[int]) -> Iterable[int]:
    i = 0
    for i in range(len(a)):
        if a[i] < 0:
            a[i] = -a[i]
        else:
            break
    left = i - 1
    right = i
    res = []
    while left >= 0 and right < len(a):
        if a[left] <= a[right]:
            res.append(a[left] * a[left])
            left -= 1
        else:
            res.append(a[right] * a[right])
            right += 1
    while left >= 0:
        res.append(a[left] * a[left])
        left -= 1
    while right < len(a):
        res.append(a[right] * a[right])
        right += 1
    return res


# given a sorted array with possibly negative and positive ints, return
# the result of squaring the ints in sorted order
assert sorted_square_num([-5, -3, -1, 0, 1, 4, 5]) == [0, 1, 1, 9, 16, 25, 25]
assert sorted_square_num([1, 2, 3]) == [1, 4, 9]
assert sorted_square_num([0, 0, 2]) == [0, 0, 4]
assert sorted_square_num([-3, -2, -1]) == [1, 4, 9]

