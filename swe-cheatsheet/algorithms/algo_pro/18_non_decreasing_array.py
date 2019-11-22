from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        decrease_count = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if decrease_count:
                    return False
                else:
                    nums[i + 1] = nums[i]
                    decrease_count = 1

        # TODO case where num is set lower than next

        return True


print(Solution().checkPossibility(nums=[3, 4, 2, 3]))
