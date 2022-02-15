from typing import List


class Solution:
    def two_sum_(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {n: i for i, n in enumerate(nums)}
        for num in num_to_index:
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[num], num_to_index[complement]]

        return [-1, -1]

    # since we know there is exactly 1 solution, we can simply do it in 1 pass

    def two_sum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = dict()
        for i, num in enumerate(nums):
            if (target - num) in num_to_index:
                return [i, num_to_index[target - num]]

            num_to_index[num] = i


print(Solution().two_sum(nums=[1, 2, 3, 20, 5, 8, 12, 22], target=42))
