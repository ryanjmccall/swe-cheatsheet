from typing import List


class Solution:

    def find_triplets(self, nums: List[int]):
        squares = {n * n for n in nums}
        for i, a in enumerate(nums):
            for b in nums[i + 1:]:
                if a * a + b * b in squares:
                    return True
        return False


print(Solution().find_triplets(nums=[3, 5, 12, 5, 13]))
