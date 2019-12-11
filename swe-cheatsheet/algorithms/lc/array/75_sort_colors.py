from collections import Counter
from typing import List


class Solution:
    def sortColors_(self, nums: List[int]) -> None:
        counter = Counter(nums)
        i = 0
        for c in (0, 1, 2):
            for _ in range(counter[c]):
                nums[i] = c
                i += 1

    def sortColors(self, nums: List[int]) -> None:
        head = 0
        i = 0
        tail = len(nums) - 1
        while i <= tail:
            if nums[i] == 0:
                nums[head], nums[i] = nums[i], nums[head]
                head += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[i], nums[tail] = nums[tail], nums[i]
                tail -= 1


def t():
    nums = [2, 0, 2, 1, 1, 0]
    Solution().sortColors(nums)
    print(nums)

t()

