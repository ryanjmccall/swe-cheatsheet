from typing import List


class Solution:
    def combinationSum_recur(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()

        def dfs(start: int, target_: int, path: List[int]):
            if target_ == 0:
                result.append(path)
                return

            for i in range(start, len(nums)):
                if target_ < nums[i]:
                    return

                dfs(i, target_ - nums[i], path + [nums[i]])

        dfs(start=0, target_=target, path=[])
        return result

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        stack = [(0, [], target)]
        while stack:
            start, path, target_ = stack.pop()
            if target_ == 0:
                result.append(path)
                continue

            for i in range(start, len(nums)):
                if target_ < nums[i]:
                    break

                stack.append((i, path + [nums[i]], target_ - nums[i]))

        return result


print(Solution().combinationSum(nums=[8, 7, 4, 3], target=11))
