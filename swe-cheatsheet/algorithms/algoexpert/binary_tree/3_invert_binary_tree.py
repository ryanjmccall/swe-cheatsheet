def invertBinaryTree(tree):
    # recursively
    if not tree:
        return

    tree.left, tree.right = tree.right, tree.left
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)

# iteratively
# q = [tree]
# for c in q:
# 	c.left, c.right = c.right, c.left
# 	if c.left:
# 		q.append(c.left)
# 	if c.right:
# 		q.append(c.right)

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
