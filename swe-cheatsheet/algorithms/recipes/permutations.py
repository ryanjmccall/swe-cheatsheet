from typing import List, Any, Iterator


def permutation_1(arr):
    if not arr:
        return []

    if len(arr) == 1:
        return [arr]

    perms = []
    for i in range(len(arr)):
        v = arr[i]
        remain = arr[:i] + arr[i + 1:]
        perms.extend([v] + p for p in permutation_1(remain))

    return perms


def permutation_2(arr: List[int]) -> List[List[int]]:
    if not arr: return []
    if len(arr) == 1: return [arr]

    perms = []
    for i in range(len(arr)):
        perms.extend([arr[i]] + p for p in permutation_2(arr=arr[:i] + arr[i+1:]))

    return perms


def permutation(arr: List[Any]) -> Iterator[List[Any]]:
    if not arr: return []
    if len(arr) == 1: return [arr]
    return (
        [arr[i]] + p
        for i in range(len(arr))
            for p in permutation(arr=arr[:i] + arr[i+1:])
    )


def test():
    for perm in permutation(arr=list('1234')):
        print(''.join(perm))


test()

