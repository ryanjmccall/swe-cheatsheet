from collections import OrderedDict


class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

    def __str__(self):
        return f'{self.key}: {self.val}'


class LRUCache_:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = dict()
        self.head = None
        self.tail = None

    def __str__(self):
        return f'lru: {self.head} mru: {self.tail} kv: {self.key_to_node}'

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            self._remove(self.key_to_node[key])

        n = Node(key, value)
        self._add(n)
        self.key_to_node[key] = n
        if len(self.key_to_node) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.key_to_node[n.key]

    def _remove(self, node: Node):
        prev = node.prev
        nxt = node.next
        if prev:
            prev.next = nxt
        if nxt:
            nxt.prev = prev

    def _add(self, node: Node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail

    def get(self, key: int) -> int:
        node = self.key_to_node.get(key)
        if not node:
            return -1

        self._remove(node)
        self._add(node)
        return node.val


class LRUCacheOrderedDict:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1

        val = self.cache[key]
        self.cache.move_to_end(key)
        return val

    def put(self, key, value):
        if key in self.cache:
            del self.cache[key]

        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = dict()
        self.next, self.before = {}, {}  # implements bidirectional links
        self.head, self.tail = '#', '$'
        self._connect(self.head, self.tail)

    def _connect(self, a, b):
        self.next[a] = b
        self.before[b] = a

    def _remove(self, k):
        self._connect(self.before[k], self.next[k])
        del self.before[k], self.next[k], self.cache[k]

    def _append(self, k, v):
        self.cache[k] = v
        self._connect(self.before[self.tail], k)
        self._connect(k, self.tail)
        if len(self.cache) > self.capacity:
            self._remove(self.next[self.head])  # TODO why?

    def get(self, key):
        if key not in self.cache:
            return -1

        val = self.cache[key]
        self._remove(key)
        self._append(key, val)
        return val

    def put(self, key, value):
        if key in self.cache:
            self._remove(key)
        self._append(key, value)


def test():
    c = LRUCache(capacity=2)
    assert c.put(1, 1) is None
    assert c.put(2, 2) is None
    assert c.get(1) == 1
    assert c.put(3, 3) is None
    assert c.get(2) == -1, c.get(2)
    assert c.put(4, 4) is None
    assert c.get(1) == -1
    assert c.get(3) == 3
    assert c.get(4) == 4


test()


"""
["LRUCache","put","put","get","put","get","put","get","get","get"]
[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

expected: [null,null,null,1,null,-1,null,-1,3,4]
"""
