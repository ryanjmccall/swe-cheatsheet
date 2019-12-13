class UnbalancedTree(Exception):
    pass

class Solution:
    def isBalanced(self, root) -> bool:

        def height(n) -> int:
            if n is None:
                return 0
            left = height(n.left)
            right = height(n.right)
            if abs(left - right) > 1:
                raise UnbalancedTree()
            return 1 + max(left, right)

        try:
            return height(root) > -1
        except UnbalancedTree:
            return False

    def isBalanced_two_vars(self, root) -> bool:
        return self._helper(root, 0)[0]

    def _helper(self, root, depth: int) -> (bool, int):
        if not root:
            return True, depth - 1

        is_left, left_depth = self._helper(root.left, depth + 1)
        is_right, right_depth = self._helper(root.right, depth + 1)
        if not is_left or not is_right:
            return False, depth + 1

        if abs(left_depth - right_depth) > 1:
            return False, depth + 1

        return True, max(left_depth, right_depth)