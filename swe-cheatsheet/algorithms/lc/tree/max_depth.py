
class TreeNode:
    def __init__(self, v):
        self.v=v
        self.left=None
        self.right=None


class Solution(object):
    def maxDepth_recur(self, n):
        return max(self.maxDepth(n.left), self.maxDepth(n.right)) + 1 if n else 0

    def maxDepth_(self, n):
        if not n: return 0
        arr, level = [n], 0
        while True:
            s = len(arr)
            for i in range(s):
                if arr[i].left: arr.append(arr[i].left)
                if arr[i].right: arr.append(arr[i].right)
            level += 1
            if len(arr) == s:
                break
            arr = arr[s:]
        return level

    def maxDepth(self, n):
        if not n: return 0
        max_depth = 1
        stack = [(n, 1)]
        while stack:
            cur, d = stack.pop()
            if cur.left:
                stack.append((cur.left, d + 1))
            if cur.right:
                stack.append((cur.right, d + 1))
            if (cur.left or cur.right) and d + 1 > max_depth:
                max_depth = d + 1
        return max_depth

def test():
    n = TreeNode(3)
    n.left = TreeNode(9)
    n.right = TreeNode(20)
    n.right.left = TreeNode(15)
    n.right.right = TreeNode(7)
    print(Solution().maxDepth(n))


test()
