



class Solution(object):
    def rotate(self, nums: list, k: int):
        k %= len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)
        return nums

    def reverse(self, nums, start, end):
        times = (end - start + 1) // 2
        for i in range(times):
            nums[start + i], nums[end - i] = nums[end - i], nums[start + i]


# print(Solution().rotate(arr=[1, 2, 3, 4, 5, 6, 7], k=3))
print(Solution().rotate(nums=[1, 2, 3, 4, 5], k=4))
