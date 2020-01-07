from typing import List


def has_pair_with_sum(arr: List[int], target: int) -> bool:
    """Returns whether list contains a pair that sums to target."""
    seen = set()
    for n in arr:
        if target - n in seen:
            return True
        seen.add(n)
    return False


print(has_pair_with_sum(arr=[-1, 1, 2, 4, 4, 9], target=8))
