class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, cap):
        self.d = dict()
        self.cap = cap
        self.head = Node('#', None)  # LRU
        self.tail = Node('$', None)  # MRU
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, k: int):
        if k in self.d:
            n = self.d[k]
            self._ll_remove(n)
            self._ll_add(n)
            return n.val
        return -1

    def _ll_remove(self, n):
        n.prev.next, n.next.prev = n.next, n.prev

    def _ll_add(self, n):
        p = self.tail.prev  # stuff n in between p and dummy tail
        p.next = n
        n.next = self.tail
        self.tail.prev = n
        n.prev = p

    def put(self, k, v):
        if k in self.d:
            self._ll_remove(self.d[k])
        elif len(self.d) >= self.cap:
            lru = self.head.next
            self._ll_remove(lru)
            del self.d[lru.key]

        n = Node(k, v)  # wasteful 
        self._ll_add(n)
        self.d[k] = n
