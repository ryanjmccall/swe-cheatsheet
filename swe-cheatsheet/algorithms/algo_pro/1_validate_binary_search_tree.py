# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Solution:
    def is_valid_bst_recur(self, root) -> bool:
        def dfs(node, lower, upper):
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False

            if not dfs(node.left, lower, val):
                return False

            if not dfs(node.right, val, upper):
                return False

            return True

        return dfs(root, float('-inf'), float('inf'))

    def is_valid_bst_iter(self, node) -> bool:
        if not node:
            return True

        stack = [(node, float('-inf'), float('inf'))]
        while stack:
            cur, lower, upper = stack.pop()
            val = cur.val
            if val <= lower or val >= upper:
                return False

            if cur.right:
                stack.append((cur.right, val, upper))

            if cur.left:
                stack.append((cur.left, lower, val))

        return True


node = TreeNode(5)
node.left = TreeNode(4)
node.right = TreeNode(7)
print(Solution().is_valid_bst_iter(node))
