from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        i = 0
        j = len(nums) - 1
        while nums[j] == val:
            nums.pop()
            j -= 1
            if j < 0:
                return 0

        while i < j:
            if nums[i] == val:
                nums[i] = nums[j]
                nums.pop()
                j -= 1

                while nums[j] == val and i < j:
                    nums.pop()
                    j -= 1
                    if j < 0:
                        return 0

            i += 1

        return i + 1


print(Solution().removeElement([3, 2, 2, 3], 3))
