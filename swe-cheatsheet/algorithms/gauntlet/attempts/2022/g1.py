"""
The Gauntlet is a set of coding tasks for algorithms commonly used in coding question solutions
written succintly in Python.
"""

from typing import List, Dict


### Section 0. Linked List

# define datastructure
class ListNode:
    def __init__(self, val: int, next: 'ListNode' = None, prev: 'ListNode' = None):
        self.val = val
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self, val: int):
        self.head = ListNode(val)
        self.tail = self.head

    def __str__(self):
        vals = []
        cur = self.head
        while cur:
            vals.append(str(cur.val))
            cur = cur.next
        _vals = ' '.join(vals)
        return f'head={self.head.val} tail={self.tail.val} vals=[{_vals}]'

    def prepend(self, val: int):
        n = ListNode(val)
        n.next = self.head
        self.head.prev = n
        self.head = n

    def append(self, val: int):
        n = ListNode(val, prev=self.tail)
        self.tail.next = n
        self.tail = self.tail.next

    def remove(self, val: int):
        cur = self.head
        while cur:
            if cur.val == val:
                cur.prev.next = cur.next
                cur.next.prev = cur.prev

                if cur == self.head:
                    self.head = cur.next
                if cur == self.tail:
                    self.tail = cur.prev

                cur.next = cur.prev = None
                return cur.val
            cur = cur.next

        return None


def test_linked_list():
    a = LinkedList(5)
    a.prepend(4)
    a.append(6)
    a.append(7)

    print(a)

    a.remove(6)

    print(a)

# test_linked_list()

# create

# traverse

# prepend

# append

# insert

# remove

### Section 1. Graph algorithms
from collections import defaultdict


def get_adjacency_list(edges: List[tuple]):
    g = defaultdict(set)
    for u, v in edges:
        g[u].add(v)
    return g


def sample_dag() -> List[tuple]:
    """
    1 > 2 > (6, 7, 8)
    1 > 3
    1 > 4 > 5
    """
    edges = [(1, 2), (1, 3), (1, 4), (4, 5), (2, 6), (2, 7), (2, 8)]
    return get_adjacency_list(edges=edges)


def sample_cycle():
    """ 0 > 1 > 2 > 3 > 1  """
    return get_adjacency_list(edges=[(0, 1), (1, 2), (2, 3), (3, 1)])


from collections import deque


# bfs_iter
def bfs_iter(root: int, g: Dict[int, set]):
    visited = set()
    q = deque([root])
    while q:
        cur = q.popleft()
        visited.add(cur)
        yield cur
        q.extend(g[cur])


def test_bfs_iter():
    g = sample_dag()
    itr = bfs_iter(1, g)
    print(' > '.join((str(x) for x in itr)))


# dfs iter
def dfs_iter(root: int, g: dict):
    visited = set()
    q = [root]
    while q:
        cur = q.pop()
        visited.add(cur)
        yield cur
        q.extend(g[cur])


def test_dfs_iter():
    g = sample_dag()
    itr = dfs_iter(1, g)
    print(' > '.join((str(x) for x in itr)))


# test_dfs_iter()

def dfs(root, g):
    visited = set()
    result = []

    def _dfs(n):
        if n in visited:
            return

        visited.add(n)
        result.append(n)
        for nbr in g[n]:
            _dfs(nbr)

    _dfs(root)
    return result


def test_dfs():
    g = sample_dag()
    itr = dfs(1, g)
    print(itr)


# test_dfs()

from itertools import chain
from collections import Counter


# topological sort
def top_sort(g) -> List[int]:
    indegree = Counter(chain.from_iterable(g.values()))
    res = []
    stack = [n for n in g if not indegree[n]]
    while stack:
        n = stack.pop()
        res.append(n)
        for v in g[n]:
            indegree[v] -= 1
            if not indegree[v]:
                stack.append(v)

    return [] if any(c for c in indegree.values()) else res


# cycle detection using top sort
def has_cycle_topo(g) -> bool:
    return not top_sort(g)


assert has_cycle_topo(sample_cycle())

# cycle detection using recursion


# dijkstra's algo


### Section 2. Tree algorithms

# TODO create the fundamental tree datastructure

def sample_tree():
    #  1
    # / \
    # 2   3
    #   / \
    #  4*  5
    # a = Node(1)
    # a.left = Node(2)
    # a.right = Node(3)
    # a.right.left = Node(4)
    # a.right.right = Node(5)
    #
    # b = Node(1)
    # b.left = Node(2)
    # b.right = Node(3)
    # b.right.left = Node(4)
    # b.right.right = Node(5)
    pass

# what is preorder?

# what is inorder?

# what is postorder?

# inorder recur

# preorder recur

# postorder recur

# inorder iter

# preorder iter

# postorder iter

### Section 3. Retrieval tree / trie
# must work for 'hi' and 'higher'

# code build_trie

# code match_trie

### Section 4. Binary heap
# methods: insert, remove_min


### Section 5. Searching
# quickselect

# binary search

# print(binary_search([1, 1, 1, 1, 2, 3, 4, 5, 5], 4))

### Section 6. Sorting

# mergesort

# partition

# quicksort

def test_sort():
    myList = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # TODO
    assert myList == [17, 20, 26, 31, 44, 54, 55, 77, 93]

### Section 7. Ordered Dict / LRU cache

# implement LRU cache using ordered dict

# implement ordered dict using dict

### Section 8. combinatorics

# permutation recur

# permutation iter


def test_permutations():
    vals = [3, 4, 5]

# combination recur

# combination iter


def test_combos():
    vals = list('1234')
