from typing import List


class Solution:
    def permute_recur(self, nums: List[int]) -> List[List[int]]:
        result = []

        def helper(left: list, right: list):
            if len(right) <= 1:
                result.append(left + right)
            else:
                for i, item in enumerate(right):
                    helper(left + [item], right[:i] + right[i + 1:])

        helper([], nums)
        return result

    def permute_iter(self, nums):
        res = []
        stack = [([], nums)]
        for left, right in stack:
            if right:
                for i, val in enumerate(right):
                    stack.append((left + [val], right[:i] + right[i+1:]))
            else:
                res.append(left)

        return res


print(Solution().permute_recur(nums=[1,2,3]))
print(Solution().permute_iter(nums=[1,2,3]))
