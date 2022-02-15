class Node:
    def __init__(self, v: int):
        self.val = v
        self.next = None


class Solution:

    def reverse(self, n: Node) -> Node:
        if not n or not n.next:
            return n

        prev = None
        current = n
        while current:
            next_node = current.next
            current.next = prev

            prev = current
            current = next_node

        return prev

    def reverse_recur(self, head: Node) -> Node:
        if not head or not head.next:
            return head

        next_node = head.next
        new_head = self.reverse_recur(next_node)
        next_node.next = head
        head.next = None
        return new_head
