# void moveZeroes(vector<int>& nums) {
#     for (int lastNonZeroFoundAt = 0, cur = 0; cur < nums.size(); cur++) {
#         if (nums[cur] != 0) {
#             swap(nums[lastNonZeroFoundAt++], nums[cur]);
#         }
#     }
# }

class Solution(object):

    def move_zeroes(self, nums):
        # if you move the zeroes, you may have to repeatedly move them,
        # but if you move the non-zeros to the left most available position, you only have to move
        # each non-zero once
        next_non_zero_index = 0
        current = 0
        while current < len(nums):
            if nums[current]:
                nums[current], nums[next_non_zero_index] = nums[next_non_zero_index], nums[current]
                next_non_zero_index += 1

            current += 1


_nums = [0,1,0,3,12]
Solution().move_zeroes(_nums)
print(_nums)
