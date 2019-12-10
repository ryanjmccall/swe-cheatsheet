class Solution:
    def isValidBST(self, root) -> bool:
        def check(n, low, high) -> bool:
            if n.val < low or n.val > high:
                return False

            return check(n.left, low, n.val - 1) and check(n.right, n.val + 1, high)

        return check(root, float('-inf'), float('inf'))