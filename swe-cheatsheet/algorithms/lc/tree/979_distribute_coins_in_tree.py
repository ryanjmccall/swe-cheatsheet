


class Solution:
    def __init__(self):
        self.moves = 0

    def distributeCoins(self, root):
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            # increase number of moves
            self.moves += abs(left) + abs(right)
            return node.val - 1 + left + right

        dfs(root)
        return self.moves



