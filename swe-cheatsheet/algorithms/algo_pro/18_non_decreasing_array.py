from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        index = None
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if index is not None:
                    # two decreases
                    return False

                index = i

        if index is None:  # zero decreases
            return True

        # one decrease
        if index in (0, len(nums) - 2):
            return True

        if nums[index] <= nums[index + 2]:
            return True

        if nums[index - 1] <= nums[index + 1]:
            # neighbors must be monotonic increasing
            return True

        return False


print(Solution().checkPossibility(nums=[2,3,3,2,4]))
