
import heapq as heap
from random import random

from typing import List


class Solution(object):
    def findKthLargest1(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]

    def findKthLargest(self, nums: list, k: int) -> int:
        return heap.nlargest(k, nums)[-1]

    def findKthLargest_quick_select(self, nums: List[int], k: int) -> int:
        index = len(nums) - k

        def select(l, r):
            if l == r:
                return nums[l]

            pivot = random.randint(l, r)
            nums[l], nums[pivot] = nums[pivot], nums[l]

            i = l
            for j in range(l + 1, r + 1):
                if nums[j] < nums[l]:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]

            nums[i], nums[l] = nums[l], nums[i]
            if index == i:
                return nums[i]
            elif index < i:
                return select(l, i - 1)
            else:
                return select(i + 1, r, )

        return select(0, len(nums) - 1)


print(Solution().findKthLargest([3,2,1,5,6,4], 2))
