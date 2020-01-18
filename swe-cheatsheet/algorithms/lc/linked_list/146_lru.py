from typing import Dict


class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None
    def __repr__(self):
        return f'{self.key}: {self.val}'

class LRUCache2:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = None  # stalest
        self.tail = None  # freshest
        self.d = dict()  # type: Dict[int, Node]

    def get(self, key: int) -> int:
        if key in self.d:
            n = self.d[key]
            v = n.val
            self._use(n)
        else:
            v = -1
        return v

    def _use(self, n: Node):
        # <head> ... <n> ... <tail>
        if self.head == self.tail:
            return

        if n == self.tail:
            self.tail = self.tail.prev

        if n.prev:
            n.prev.next = n.next
        if n.next:
            n.next.prev = n.prev
        n.prev = None
        n.next = self.head
        self.head.prev = n
        self.head = n

    def put(self, key: int, v: int) -> None:
        # update dict setting up Node
        if key in self.d:
            n = self.d[key]
            n.val = v
            self._use(n)
        else:
            if len(self.d) == self.cap:
                # if capacity exceeded evict the tail
                # <n> <tail> None
                if self.tail:
                    del self.d[self.tail.key]
                    prev = self.tail.prev
                    self.tail.prev = None
                    if prev:
                        prev.next = None
                    self.tail = prev

            n = Node(key, v)
            self.d[key] = n
            if self.head:
                n.next = self.head
                self.head.prev = n

            if not self.tail:
                self.tail = n

            self.head = n


class LRUCache:

    def __init__(self, capacity: int):
        self.dic = {}
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self._remove(node)
            self._add(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        if key in self.dic:
            node = self.dic[key]
            self._remove(node)
            node = Node(key, value)
            self._add(node)
            self.dic[key] = node
        else:
            if len(self.dic) >= self.capacity:
                temp = self.head.next
                self._remove(temp)
                del self.dic[temp.key]

            node = Node(key, value)
            self._add(node)
            self.dic[key] = node

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        node.next = self.tail
        self.tail.prev = node
        node.prev = p


def test():
    c = LRUCache(2)
    c.put(2, 1)
    c.put(3, 2)
    assert c.get(3) == 2
    assert c.get(2) == 1
    c.put(4, 3)
    assert c.get(2) == 1
    assert c.get(3) == -1
    assert c.get(4) == 3


test()
