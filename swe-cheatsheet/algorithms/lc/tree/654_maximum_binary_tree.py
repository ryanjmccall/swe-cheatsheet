# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return f'{self.left} < {self.val} > {self.right}'


class Solution:
    def _constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        idx = self._get_max_idx(nums)
        root = TreeNode(val=nums[idx])
        left_nums = nums[:idx]
        if left_nums:
            root.left = self._constructMaximumBinaryTree(left_nums)

        right_nums = nums[idx + 1:]
        if right_nums:
            root.right = self._constructMaximumBinaryTree(right_nums)

        return root

    def _get_max_idx(self, nums: List[int]) -> int:
        max_idx = 0
        max_val = -float('inf')
        for i, num in enumerate(nums):
            if num > max_val:
                max_idx = i
                max_val = num

        return max_idx

    def constructMaximumBinaryTree(self, nums):
        stack = [TreeNode(nums[0])]
        for num in nums[1:]:
            node = TreeNode(num)
            if num < stack[-1].val:
                stack[-1].right = node
            else:
                while stack and stack[-1].val < num:
                    node.left = stack.pop()
                if stack:
                    stack[-1].right = node

            stack.append(node)

        return stack[0]


def main():
    root = Solution().constructMaximumBinaryTree(nums=[3, 2, 1, 6, 0, 5])
    print(root)


main()
