from collections import deque


class Node:
    def __init__(self, v: int, left=None, right=None):
        self.v = v
        self.left = left
        self.right = right


def zigzag(root: Node):
    res = []
    cur_level = [root]
    next_level = []
    l2r = False

    while cur_level:
        n = cur_level.pop()
        res.append(n.v)

        if l2r:
            if n.left:
                next_level.append(n.left)
            if n.right:
                next_level.append(n.right)
        if not l2r:
            if n.right:
                next_level.append(n.right)
            if n.left:
                next_level.append(n.left)

        if not cur_level:
            l2r = not l2r
            cur_level = next_level
            next_level = []

    return res



def zigzag2(node):
    q, flag = deque([node]), False
    while q:
        for _ in range(len(q)):
            n = q.popleft() if flag else q.pop()
            yield n.v
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
        flag = not flag


tree = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
print(zigzag(tree))
print(list(zigzag2(tree)))
