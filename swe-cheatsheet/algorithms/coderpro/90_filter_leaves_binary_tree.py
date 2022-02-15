from typing import Any, Optional


class Node:
    def __init__(self, val: Any, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        s = ''
        if self.left:
            s += f'({self.left})'
        s += f'{self.val}'
        if self.right:
            s += f'({self.right})'
        return s


def filter_tree(n: Node, val: int) -> Optional[Node]:
    if not n:
        return None

    n.left = filter_tree(n.left, val)
    n.right = filter_tree(n.right, val)
    return None if n.val != val and not n.left and not n.right else n



lsub = Node(2, left=Node(2))
rsub = Node(1, left=Node(1))
_tree = Node(1, lsub, rsub)
print(filter_tree(_tree, val=2))

