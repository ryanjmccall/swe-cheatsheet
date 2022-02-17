
from typing import List

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'({self.left}) < {self.val} > ({self.right})'


def get_cousins1(root: Node, val: int) -> list:
    # this doesn't work b/c we have to exclude the siblings to compute cousins
    level = [root]
    while level:
        next_level = []
        for cur in level:
            if cur.val == val:
                return [n for n in level if n.val != val]

            if cur.left:
                next_level.append(cur.left)
            if cur.right:
                next_level.append(cur.right)
        level = next_level
    return []


def get_cousins(root: Node, val: int) -> List[Node]:
    depth, parent = depth_and_parent(root, val)
    return nodes_at_depth(root, depth, exclude=parent)


def nodes_at_depth(root: Node, depth: int, exclude: Node) -> List[Node]:
    nodes = list()

    def dfs(n: Node, cur_depth: int):
        if not n or n == exclude:
            return

        if cur_depth == depth:
            nodes.append(n)
            return

        dfs(n.left, cur_depth + 1)
        dfs(n.right, cur_depth + 1)

    dfs(root, cur_depth=0)
    return nodes


def depth_and_parent(n: Node, val: int) -> (int, Node):
    stk = [(n, 0, None)]
    while stk:
        cur, depth, parent = stk.pop()
        if cur.val == val:
            return depth, parent
        if cur.left:
            stk.append((cur.left, depth + 1, cur))
        if cur.right:
            stk.append((cur.right, depth + 1, cur))

    return -1, None


def test():
    _lsub = Node(2, Node(4), Node(6))
    _rsub = Node(3, None, Node(5))
    _tree = Node(1, _lsub, _rsub)
    print(get_cousins(_tree, 5))


if __name__ == "__main__":
    test()
