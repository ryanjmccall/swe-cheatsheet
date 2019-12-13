


class Solution:
    def countUnivalSubtrees(self, root) -> int:
        count = 0
        def dfs(root):
            nonlocal count
            if not root: return set()
            vals = {root.val}
            if root.left: vals |= dfs(root.left)
            if root.right: vals |= dfs(root.right)
            if len(vals) == 1:
                count += 1
            return vals
        dfs(root)
        return count


    def countUnivalSubtrees_mine(self, root) -> int:
        self.count = 0
        def dfs(n, parent_val: int) -> bool:
            if not n: return True
            left = dfs(n.left, n.val)
            right = dfs(n.right, n.val)
            if left and right:
                self.count += 1
            return n.val == parent_val and left and right
        if root:
            dfs(root, root.val)
        return self.count

    def countUnivalSubtrees_another_way(self, root) -> int:
        self.count = 0

        def helper(root):
            if not root:
                return
            left = helper(root.left)
            right = helper(root.right)
            if (not left or left == root.val) and (not right or right == root.val):
                self.count += 1
                return root.val

            # If current tree is not univalued, the parent tree cannot be univalued either.
            # So we return a value that the parent tree's root node can never match.
            return '#'

        helper(root)
        return self.count








