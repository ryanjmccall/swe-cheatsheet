"""
The Gauntlet is a set of coding tasks for algorithms commonly used in coding question solutions
written succintly in Python.
"""

from typing import List, Any, Tuple, Generator


### Section 0. Linked List

class ListNode:
    def __init__(self, v, prev: 'ListNode' = None, nxt: 'ListNode' = None):
        self.v = v
        self.prev = prev
        self.nxt = nxt

    def __repr__(self):
        return f'{self.v} {self.prev} {self.nxt}'


class LinkedList:
    def __init__(self, a: List[Any]):
        self.head = None
        self.tail = None
        if not a:
            return

        self.head = ListNode(a[0])
        cur = self.head
        for v in a[1:]:
            cur.nxt = ListNode(v, prev=cur)
            cur = cur.nxt
        self.tail = cur

    def prepend(self, v):
        self.head.prev = ListNode(v, nxt=self.head)
        self.head = self.head.prev

    def append(self, v):
        self.tail.nxt = ListNode(v, prev=self.tail)
        self.tail = self.tail.nxt

    def remove(self, v: Any) -> bool:
        cur = self.head
        while cur:
            if cur.v == v:
                # update head, tail, remove nbr ptrs, remove cur's ptrs
                prev = cur.prev
                nxt = cur.nxt
                if prev == self.head:
                    self.head = nxt
                if nxt == self.tail:
                    self.tail = prev
                prev.nxt = nxt
                nxt.prev = prev
                cur.nxt = None
                cur.prev = None
                return True

            cur = cur.nxt

        return False


### Section 1. Graph algorithms
from collections import defaultdict


def get_adjacency_list(edges: List[Tuple[int, int]]) -> dict:
    g = defaultdict(list)
    for u, v in edges:
        g[u].append(v)
    return g


def sample_dag() -> dict:
    """
    1 > 2 > (6, 7, 8)
    1 > 3
    1 > 4 > 5
    """
    edges = [(1, 2), (1, 3), (1, 4), (4, 5), (2, 6), (2, 7), (2, 8)]
    return get_adjacency_list(edges)


def sample_dcg():
    """ 0 > 1 > 2 > 3 > 1  """
    return get_adjacency_list(edges=[(0, 1), (1, 2), (2, 3), (3, 1)])


from collections import deque


def bfs(g: dict, root: int) -> Generator[int, None, None]:
    if root not in g:
        return
    seen, q = set(), deque([root])  # maintains frontier of unvisited nodes
    while q:
        cur = q.popleft()
        seen.add(cur)
        yield cur
        q.extend(n for n in g[cur] if n not in seen)


# print(list(bfs(sample_dag(), 1)))


# dfs recur
def dfs_recur(g: dict, root: int):
    seen = set()

    def _dfs(n: int):
        seen.add(n)
        yield n
        for v in g[n]:
            if v not in seen:
                yield from _dfs(v)

    if root in g:
        yield from _dfs(root)


# print(list(dfs_recur(sample_dag(), 1)))
# print(list(dfs_recur(sample_dag(), -1)))


# dfs iter
def dfs_iter(g: dict, root: int):
    if root not in g:
        return
    seen = set()
    stk = [root]
    while stk:
        cur = stk.pop()
        seen.add(cur)
        yield cur
        stk.extend(n for n in g[cur] if n not in seen)


# print(list(dfs_iter(sample_dag(), 1)))


# cycle detection using recursion
def has_cycle(g: dict, root: int):
    seen = set()

    def dfs(n: int) -> bool:
        seen.add(n)
        for nbr in g[n]:
            if nbr in seen or dfs(nbr):
                return True

        seen.remove(n)
        return False

    return any(dfs(v) for v in g if v not in seen)

# bonus: topological sort
# cycle detection using top sort

# graph path to value

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

# create BST from an array

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
