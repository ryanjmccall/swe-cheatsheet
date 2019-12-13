from typing import List


class Solution:
    def minSubArrayLen_(self, target: int, nums: List[int]) -> int:
        if not nums: return 0
        i = 0
        j = -1
        total = 0
        min_len = float('inf')
        while j < len(nums):
            if total < target:
                j += 1
                if j == len(nums):
                    break
                total += nums[j]
            else:  # >= target
                total -= nums[i]
                i += 1

            if total >= target:
                min_len = min(min_len, j - i + 1)
                if min_len == 1:
                    return 1

        return 0 if min_len == float('inf') else min_len

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        min_len = float('inf')
        for right, n in enumerate(nums):
            total += n
            while total - nums[left] >= target:
                total -= nums[left]
                left += 1

            if total >= target:
                min_len = min(min_len, right - left + 1)

        return 0 if min_len == float('inf') else min_len


print(Solution().minSubArrayLen_(7, [2,3,1,2,4,3]))
print(Solution().minSubArrayLen(7, [2,3,1,2,4,3]))
