class Solution:
    def maxSubArray(self, nums) -> int:
        if not nums: return 0
        max_sum = nums[0]
        cur_sum = 0
        for n in nums:
            if cur_sum + n < 0:
                cur_sum = 0
                max_sum = max(max_sum, n)  # case: all negative
            else:
                cur_sum += n
                max_sum = max(max_sum, cur_sum)

        return max_sum


print(Solution().maxSubArray([-1, -4, 3, 8, 1]))
