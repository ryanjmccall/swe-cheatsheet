from collections import deque


class Node:
    def __init__(self, v):
        self.val = v
        self.children = []

    def __str__(self):
        return self.val


def print_by_level(n: Node):
    prev_level = 0
    res = ''
    queue = deque([(n, 0)])
    while queue:
        cur, level = queue.popleft()
        if level > prev_level:
            prev_level = level
            res += '\n'
        res += str(cur.val)
        queue.extend((c, level + 1) for c in cur.children)
    return res


def print_by_level2(n: Node):
    res = ''
    q = deque([n])
    while q:
        for _ in range(len(q)):
            cur = q.popleft()
            res += str(cur.val)
            q.extend(cur.children)
        res += '\n'
    return res


def t():
    n = Node('a')
    n.children = [Node('b'), Node('c')]
    n.children[0].children = [Node('g')]
    n.children[1].children = [Node('d'), Node('e'), Node('f')]
    print(print_by_level(n))
    print(print_by_level2(n))


t()
