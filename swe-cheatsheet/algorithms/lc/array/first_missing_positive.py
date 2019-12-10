class Solution:
    def firstMissingPositive(self, nums) -> int:
        nums = [0] + nums
        for n in nums[1:]:
            if n != nums[n]:
                n, nums[n] = nums[n], n

        for i, n in enumerate(nums):
            if i != n:
                return i
        return -1


print(Solution().firstMissingPositive([3,4,-1,1]))
