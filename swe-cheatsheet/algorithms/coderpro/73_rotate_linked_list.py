

class Node(object):
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt

    def __repr__(self):
        return f'{self.val}, {self.nxt}'


def rotate(node: Node, times: int) -> Node:
    # time: O(n) + O(n) + O(1) = O(n)
    # space: O(1)
    if not times:
        return node

    length = 0
    cur = node
    while cur:
        length += 1
        cur = cur.nxt
    fast_advance = times % length

    fast, slow = node, node
    for _ in range(fast_advance):
        fast = fast.nxt

    while fast.nxt:
        fast = fast.nxt
        slow = slow.nxt

    fast.nxt = node
    head = slow.nxt
    slow.nxt = None
    return head


node = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(rotate(node, 2))
# 4, 5, 1, 2, 3
