from typing import List
from functools import cmp_to_key


def get_largest_number(nums: List[int]) -> str:
    # space: O(n) worst case sub divide
    # time: O(nlog(n))
    key = cmp_to_key(
        lambda x, y: 1 if str(x) + str(y) < str(y) + str(x) else -1  # want largest to smallest reverse order
    )
    sorted_vals = sorted(nums, key=key)
    res = ''.join(map(str, sorted_vals))
    return '0' if res[0] == '0' else res


a = [17, 7, 2, 45, 72]

print(get_largest_number(a))

