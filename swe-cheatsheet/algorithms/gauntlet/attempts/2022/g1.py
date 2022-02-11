"""
The Gauntlet is a set of coding tasks for algorithms commonly used in coding question solutions
written succintly in Python.
"""

from typing import List, Dict, Iterable, Generator, Any


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

def dfs_recur(root, g):
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
    itr = dfs_recur(1, g)
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
def has_cycle_recur(g) -> bool:
    visited = set()

    def dfs(n: int):
        visited.add(n)
        for e in g[n]:
            if e in visited or dfs(e):
                return True

        visited.remove(n)
        return False

    return any(dfs(v) for v in g if v not in visited)


# graph path to value
def graph_path(g, start: int, goal: int) -> List[int]:
    visited = set()
    path = []

    def dfs(n: int):
        visited.add(n)
        path.append(n)

        if n == goal:
            return path

        for v in g[n] - visited:
            sub = dfs(v)
            if sub is not None:
                return sub

        visited.remove(n)
        path.pop()
        return None

    return dfs(start)



assert graph_path(g=sample_dag(), start=1, goal=5) == [1, 4, 5]


# dijkstra's algo


### Section 2. Tree algorithms

class Node(object):
    def __init__(self, val: int, left: 'Node' = None, right: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right


def sample_tree():
    #   1
    #  / \
    # 2   3
    #    / \
    #   4   5
    a = Node(1)
    a.left = Node(2)
    a.right = Node(3)
    a.right.left = Node(4)
    a.right.right = Node(5)

    b = Node(1)
    b.left = Node(2)
    b.right = Node(3)
    b.right.left = Node(4)
    b.right.right = Node(5)

# what is preorder? visit root before l, r: root > left > right

# what is inorder? visit root b/w l, r: left > root > right

# what is postorder? visit root after l, r: left > right > root


# preorder recur
def preorder_recur(n: Node) -> Generator[Node, None, None]:
    if not n:
        return
    yield n.val
    if n.left:
        yield from preorder_recur(n.left)
    if n.right:
        yield from preorder_recur(n.right)


# inorder recur
def inorder_recur(n: Node) -> Generator[Node, None, None]:
    if not n:
        return
    if n.left:
        yield from inorder_recur(n.left)
    yield n.val
    if n.right:
        yield from inorder_recur(n.right)


# postorder recur
def postorder_recur(n: Node) -> Generator[Node, None, None]:
    if n.left:
        yield from postorder_recur(n.left)
    if n.right:
        yield from postorder_recur(n.right)
    yield from n.val


# preorder iter
def preorder_iter(n: Node) -> Generator[Node, None, None]:
    stk = [n]
    while stk:
        cur = stk.pop()
        yield cur.val
        if cur.right:
            stk.append(cur.right)
        if cur.left:
            stk.append(cur.left)


# inorder iter
def inorder_iter(n: Node) -> Generator[Node, None, None]:
    stk = []
    cur = n
    while stk or cur:
        if cur:
            # skip visiting cur until left fully explored
            stk.append(cur)
            cur = cur.left
            continue

        cur = stk.pop()
        yield cur.val
        cur = cur.right


# postorder iter
def postorder_iter(n: Node) -> Generator[Node, None, None]:
    stk = []
    cur = n
    last = None
    while stk or cur:
        if cur:
            stk.append(cur)
            cur = cur.left
        else:
            peek = stk[-1]
            if peek.right and peek.right != last:
                cur = peek.right
            else:
                last = stk.pop()
                yield last.val


def test_tree():
    #  1
    # / \
    # 2   3
    #   / \
    #  4*  5
    a = Node(1)
    a.left = Node(2)
    a.right = Node(3)
    a.right.left = Node(4)
    a.right.right = Node(5)

    b = Node(1)
    b.left = Node(2)
    b.right = Node(3)
    b.right.left = Node(4)
    b.right.right = Node(5)

    print(list(preorder_recur(a)))
    print(list(preorder_iter(a)))


# test_tree()

def to_bst(a: List[int]):
    if not a:
        return None

    mid = len(a) // 2
    root = Node(a[mid])
    root.l, root.r = to_bst(a[:mid]), to_bst(a[mid+1:])
    return root

### Section 3. Retrieval tree / trie
# must work for 'hi' and 'higher'


class TrieNode(object):
    def __init__(self):
        self.terminal = False
        self.children = dict()  # type: Dict[str, TrieNode]


class Trie(object):
    def __init__(self, words: List[str]):
        self.root = TrieNode()
        for w in words:
            cur = self.root
            for c in w:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.terminal = True

    def matches(self, prefix: str) -> Generator[str, None, None]:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return
            cur = cur.children[c]

        stk = [(cur, prefix)]
        while stk:
            cur, pre = stk.pop()
            if cur.terminal:
                yield pre
            stk.extend(((child, pre + char) for char, child in cur.children.items()))


def test_trie():
    t = Trie(words=['cat', 'car', 'dog'])
    for pre in ('ca', 'd', 'zz'):
        print(list(t.matches(pre)))


# test_trie()

# code build_trie

# code match_trie

### Section 4. Binary heap
# methods: insert, remove_min
class BinaryHeap(object):
    def __init__(self):
        self.a = [0]

    @property
    def size(self) -> int:
        return len(self.a) - 1

    def insert(self, v):
        self.a.append(v)
        self._sift_up(i=self.size)

    def _sift_up(self, i: int):
        while i // 2:
            par = i // 2
            if self.a[par] > self.a[i]:
                self.a[par], self.a[i] = self.a[i], self.a[par]
            i //= 2

    def from_list(self, a):
        self.a = [0] + list(a)
        for i in range(len(a) // 2, 0, -1):  # sift down working bottom up
            self._sift_down(i)

    def remove_min(self):
        r = self.a[1]
        self.a[1] = self.a.pop()
        self._sift_down(1)
        return r

    def _sift_down(self, i: int):
        while i * 2 <= self.size:
            min_child = self._min_child(i)
            if self.a[i] > self.a[min_child]:
                self.a[i], self.a[min_child] = self.a[min_child], self.a[i]
            i = min_child

    def _min_child(self, i: int) -> int:
        left = i * 2
        right = left + 1
        if right > self.size:
            return left
        return left if self.a[left] < self.a[right] else right


### Section 5. Searching
def partition(a, left, right) -> int:
    """Select a pivot value and then partitions array between left and right based on pivot"""
    pivot = a[right]
    i = left
    for j in range(left, right):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[right] = a[right], a[i]
    return i


# quickselect
def quickselect(a: List[int], target: int) -> int:
    # find the target element in an unordered list
    target = len(a) - target
    left = 0
    right = len(a) - 1
    while left < right:
        index = partition(a, left, right)
        val = a[index]
        if val < target:
            left = index + 1
        elif val > target:
            right = index - 1
        else:
            return index
    return -1


# binary search
def binary_search(a, target: int) -> int:
    l, r = 0, len(a) - 1
    while l < r:
        mid = (l + r) // 2
        if a[mid] < target:
            l = mid + 1
        elif a[mid] > target:
            r = mid - 1
        else:
            return mid
    return -1

# print(binary_search([1, 1, 1, 1, 2, 3, 4, 5, 5], 4))

### Section 6. Sorting


class Sort(object):
    @classmethod
    def qsort(cls, a, left: int, right: int):
        if left < right:
            i = partition(a, left, right)
            cls.qsort(a, left, i - 1)
            cls.qsort(a, i + 1, right)

    @classmethod
    def mergesort(cls, a):
        if len(a) <= 1:
            return
        mid = len(a) // 2
        left, right = a[:mid], a[mid:]
        cls.mergesort(left)
        cls.mergesort(right)
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1

# mergesort

# partition

# quicksort

def test_sort():
    myList = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    Sort().mergesort(myList)
    assert myList == [17, 20, 26, 31, 44, 54, 55, 77, 93]

### Section 7. Ordered Dict / LRU cache

# implement LRU cache using ordered dict

# implement ordered dict using dict


class DoubleNode(object):
    def __init__(self, k, v, prev=None, next=None):
        self.k = k
        self.v = v
        self.prev = prev
        self.next = next


class OrderedDict(object):
    # -> head  ->   tail ->  (default LIFO)
    def __init__(self):
        self.d = dict()  # type: Dict[Any, DoubleNode]
        self.head = None
        self.tail = None

    def set(self, k, v):
        if k not in self.d:
            self.d[k] = DoubleNode(k, v)
            if not self.head:
                self.head = self.d[k]
            if not self.tail:
                self.tail = self.d[k]
        else:
            self.d[k].v = v
        self.move_to_end(k, last=False)  # move to front

    def get(self, k):
        return self.d[k].v

    def popitem(self, last: bool = True):
        if not self.d:
            return

        result = self.tail if last else self.head
        del self.d[result.k]
        if last:
            self.tail, self.tail.prev = self.tail.prev, None
            self.tail.next = None
        else:
            self.head, self.head.next = self.head.next, None
            self.head.prev = None

        return result

    def move_to_end(self, k, last: bool = True):
        node = self.d[k]
        # remove node from linked list
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        node.next = None
        node.prev = None

        # then add node to head or tail
        if last:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node


### Section 8. combinatorics

# permutation recur

# permutation iter

class Permutation(object):
    def permute_recur(self, vals):
        if not vals:
            return []
        res = []

        def dfs(left, right):
            # given left/completed, right/pending, how to add from right
            if not right:
                res.append(left)
                return

            for i, v in enumerate(right):
                dfs(left=left + [v], right=right[:i] + right[i+1:])

        dfs([], vals)
        return res

    def permute_iter(self, vals):
        if not vals:
            return []
        stk = [([], vals)]
        for l, r in stk:
            for i, v in enumerate(r):
                remain = r[:i] + r[i+1:]
                if remain:
                    stk.append((l + [v], remain))
                else:
                    yield l + [v]


def test_permutations():
    vals = [3, 4, 5]
    print(Permutation().permute_recur(vals))
    print(list(Permutation().permute_iter(vals)))


# test_permutations()


# combination recur

# combination iter

class Combination:
    def combos_recur(self, left: list, right: list):
        for i, v in enumerate(right):
            yield left + [v]
            yield from self.combos_recur(left + [v], right[i+1:])

    def combos_iter(self, vals):
        stk = [([], vals)]
        for l, r in stk:
            for i, v in enumerate(r):
                yield l + [v]
                stk.append((l + [v], r[i+1:]))


def test_combos():
    combo = Combination()
    res = combo.combos_recur(left=[], right=list('1234'))
    print('\n'.join(''.join(c) for c in res))
    print()
    res = combo.combos_iter(vals=list('1234'))
    print('\n'.join(''.join(c) for c in res))


# test_combos()
