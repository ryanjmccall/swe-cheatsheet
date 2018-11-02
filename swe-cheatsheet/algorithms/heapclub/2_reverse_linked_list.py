#!/usr/bin/env python

class Node:
    def __init__(self, v):
        self.next = None
        self.val = v

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, v):
        n = Node(v)
        n.next = self.head
        self.head = n

    def __str__(self):
        vals = []
        cur = self.head
        while cur:
            vals.append(str(cur.val))
            cur = cur.next

        return ", ".join(vals)

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

def genLinkedList(size: int) -> LinkedList:
    a = LinkedList()
    for i in range(size):
        a.append(i)

    return a


def testReverseLinkedList():
    a = genLinkedList(6)
    print(a)
    a.reverse()
    print(a)


if __name__ == "__main__":
    testReverseLinkedList()
