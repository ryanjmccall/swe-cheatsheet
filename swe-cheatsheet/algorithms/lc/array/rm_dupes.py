from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums = nums[:i] + nums[i + 1:]
            else:
                i += 1

        return len(nums)


x = [1, 1, 2]
print(Solution().removeDuplicates(x))
print(x)
