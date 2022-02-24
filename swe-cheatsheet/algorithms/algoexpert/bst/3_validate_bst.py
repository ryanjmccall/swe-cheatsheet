# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(n: BST) -> bool:
    """
    Let n = total BST nodes
    Time: O(n)
    Space: O(n) worst case
    """
    return _validate(n, min_val=float('-inf'), max_val=float('inf'))


def _validate(n: BST, min_val, max_val):
    if not n:
        return True
    if n.value > max_val or n.value < min_val:
        return False

    if not _validate(n.left, min_val, n.value - 1):
        return False

    return _validate(n.right, n.value, max_val)
