
class Solution:

    def sort_three_(self, nums: list) -> list:
        from collections import Counter
        cnt = Counter(nums)
        return [1] * cnt[1] + [2] * cnt[2] + [3] * cnt[3]

    def sort_three(self, nums: list) -> list:
        if len(nums) <= 1:
            return nums

        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] == 1:
                i += 1
            elif nums[j] == 1:
                self.swap(i, j, nums)
                i += 1
            else:
                j -= 1

        return nums

    def swap(self, i, j, nums):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    def sort_nums(self, nums):
        one_index = 0
        three_index = len(nums) - 1
        index = 0
        while index <= three_index:
            if nums[index] == 1:
                nums[index], nums[one_index] = nums[one_index], nums[index]
                index += 1
                one_index += 1

            elif nums[index] == 2:
                index += 1

            elif nums[index] == 3:
                nums[index], nums[three_index] = nums[three_index], nums[index]
                three_index -= 1

        return nums


print(
    Solution().sort_nums([3, 3, 2, 1, 3, 2, 1])
)
