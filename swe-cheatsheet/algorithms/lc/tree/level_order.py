# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        results = []
        level = []
        last_depth = 0
        q = deque([root, 0])
        while q:
            cur, depth = q.popleft()
            if depth == last_depth:
                if cur.left:
                    q.append((cur.left, depth + 1))
                if cur.right:
                    q.append((cur.right, depth + 1))
            else:
                last_depth = depth
                results.append(level)
                level = list()

            level.append(cur.val)

        if level: results.append(level)
        return results