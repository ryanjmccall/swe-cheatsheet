def nodeDepths(root):
    def dfs(n, depth):
        if n:
            yield depth
            yield from dfs(n.left, depth + 1)
            yield from dfs(n.right, depth + 1)

    return sum(dfs(root, 0))


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
