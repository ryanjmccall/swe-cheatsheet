class Node(object):
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt

    def __str__(self):
        return f'{self.val}, {self.nxt}'

    def __repr__(self):
        return f'{self.val}'


def swap_every_two2(n: Node):
    if not n or not n.nxt:
        return n

    head = n.nxt
    prev = None
    a, b = n, n.nxt
    while b:
        # swap
        nxt = b.nxt
        if prev:
            prev.nxt = b
        b.nxt = a
        a.nxt = nxt

        # advance two nodes if possible
        if not nxt or not nxt.nxt:
            break

        prev, a, b = a, nxt, nxt.nxt

    return head


def swap_every_two(n):
    cur = n
    while cur and cur.next:
        cur.val, cur.nxt.val = cur.nxt.val, cur.val
        cur = cur.nxt.nxt
    return n


def swap_two(head):
    prev, cur = None, head
    while cur:
        nxt = cur.nxt
        if nxt:
            cur.nxt = nxt.nxt
            nxt.nxt = cur
            if prev:
                prev.nxt = nxt
            else:
                head = nxt
        prev, cur = cur, cur.nxt
    return head


# print(str(swap_every_two(Node(1, Node(2, Node(3, Node(4, Node(5, Node(6)))))))))
print(swap_two(Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))))
