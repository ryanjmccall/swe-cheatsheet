class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    return _helper(tree)[0]


def _helper(tree) -> (int, int):
    if not tree:
        return 0, 0

    ldiameter, lheight = _helper(tree.left)
    rdiameter, rheight = _helper(tree.right)
    # either through this node or not through this node i.e. down in a subtree
    max_diameter = max(lheight + rheight, ldiameter, rdiameter)
    return max_diameter, max(lheight, rheight) + 1
