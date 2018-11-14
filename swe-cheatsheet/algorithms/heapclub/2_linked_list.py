#!/usr/bin/env python

class Node:
    def __init__(self, v):
        self.next = None
        self.val = v

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def _getNode(self, index: int) -> (Node, Node):
        assert 0 <= index < self.size
        prev = None
        current = self.head
        for _ in range(self.size - 1 - index):
            prev = current
            current = current.next
        return current, prev

    def insert(self, n: Node, index: int):
        current, _ = self._getNode(index)
        if current:
            n.next = current.next
            current.next = n
        else:
            self.head = n

        self.size += 1

    def removeAt(self, index: int):
        current, prev = self._getNode(index)
        if prev:
            prev.next = current.next
        else:
            self.head = current.next

        current.next = None
        self.size -= 1
        return current

    def append(self, v):
        self.insert(Node(v), self.size)

    def removeLast(self) -> Node:
        return self.removeAt(self.size)

    def removeFirst(self) -> Node:
        return self.removeAt(0)

    def reverse(self):
        prev = None
        current = self.head
        while current:
            # invariant: prev is correct and current's next requires reversal
            nextNode = current.next
            current.next = prev

            prev = current
            current = nextNode

        # when loop terminates, current is None and prev is correct
        self.head = prev

    def size(self) -> int:
        return self.size

    def __str__(self):
        vals = []
        cur = self.head
        while cur:
            vals.append(str(cur.val))
            cur = cur.next

        return ", ".join(vals)


def genLinkedList(size: int) -> LinkedList:
    a = LinkedList()
    for i in range(size):
        a.append(i)

    return a


def run():
    a = genLinkedList(6)
    print(a)
    a.reverse()
    print(a)

    b = LinkedList()
    b.insert(Node(5), 0)


if __name__ == "__main__":
    run()
