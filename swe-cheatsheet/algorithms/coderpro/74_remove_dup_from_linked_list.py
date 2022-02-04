class Node(object):
    def __init__(self, val, next: 'Node' = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val} {self.next}'


def remove_duplicates(head: Node):
    if not head:
        return None

    seen = set()
    prev = None
    cur = head
    while cur:
        if cur.val in seen:
            prev.next = cur.next
            tmp = cur
            cur = cur.next
            tmp.next = None
        else:
            seen.add(cur.val)
            prev = cur
            cur = cur.next


ll = Node(1, Node(2, Node(2, Node(3, Node(3)))))
remove_duplicates(ll)
print(ll)
