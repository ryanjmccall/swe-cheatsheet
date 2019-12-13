class Solution:
    def invertTree(self, root):
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur:
                cur.left, cur.right = cur.right, cur.left
                stack.extend((cur.left, cur.right))
        return root

    def invertTree_recur(self, n):
        if n:
            n.left, n.right = self.invertTree(n.right), self.invertTree(n.left)
        return n
