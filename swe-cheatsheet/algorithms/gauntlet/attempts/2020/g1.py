# Elapsed time: 1 day
from typing import List, Set, Dict, Tuple

from collections import defaultdict, deque


# Graph
def get_adjacency_list(edges: List[Tuple[int, int]]) -> Dict[int, Set[int]]:
    g = defaultdict(set)
    for u, v in edges:
        g[u].add(v)
    return g


def sample_graph():
    # 1 > 2 > (6, 7, 8)
    # 1 > 3
    # 1 > 4 > 5
    edges = [(1, 2), (1, 3), (1, 4), (4, 5), (2, 6), (2, 7), (2, 8)]
    return get_adjacency_list(edges)

def cycle_graph():
    return get_adjacency_list(edges=[(0, 1), (1, 2), (2, 3), (3, 1)])

# bfs/dfs iter
def graph_iter(g, start: int, is_bfs: bool=True) -> List[int]:
    q = deque([start])
    visited = set()
    res = []
    while q:
        cur = q.popleft() if is_bfs else q.pop()
        visited.add(cur)
        res.append(cur)
        q.extend(nbr for nbr in g[cur] - visited)
    return res


# dfs recur
def graph_dfs_recur(g, start: int) -> List[int]:
    visited = set()
    res = []
    _graph_dfs(g, start, visited, res)
    return res


def _graph_dfs(g, start: int, visited: set, res: list):
    if start in visited:
        return

    visited.add(start)
    res.append(start)
    for nbr in g[start] - visited:
        _graph_dfs(g, nbr, visited, res)


# topological sort
def top_sort(g) -> List[int]:
    indegree = defaultdict(int)
    for sinks in g.values():
        for s in sinks:
            indegree[s] += 1

    res = []
    stk = [n for n in g if not indegree[n]]
    while stk:
        cur = stk.pop()
        res.append(cur)
        for nbr in g[cur]:
            indegree[nbr] -= 1
            if not indegree[nbr]:
                stk.append(nbr)

    return [] if any(c for c in indegree.values()) else res


# cycle detection (recur & top)
def has_cycle(g) -> bool:
    if not g: return False
    return len(top_sort(g)) == 0


def graph_cycle_recur(g) -> bool:
    visited = set()
    def dfs(node: int):
        visited.add(node)
        for nbr in g[node]:
            if nbr in visited or dfs(nbr):
                return True

        visited.remove(node)
        return False

    return any(dfs(v) for v in g if v not in visited)


def graph_path(g, start: int, goal: int) -> List[int]:
    visited = set()
    def dfs(node: int, path):
        if node == goal:
            return path + [node]

        visited.add(node)
        path.append(node)
        for nbr in g[node] - visited:
            res = dfs(nbr, path)
            if res is not None:
                return res

        visited.remove(node)
        path.pop()
        return None

    return dfs(start, [])


# - dijkstra
def dijkstra_shortest_paths(g, start: int):  # 13 lines
    def extract_min(q): return 0
    def decrease_key(q, k, c): pass
    distance = {v: float('inf') for v in g}
    distance[start] = 0
    previous = {v: None for v in g}
    queue = list(g)
    while queue:
        source = extract_min(queue)
        for sink, weight in g[source]:
            cost = distance[source] + weight
            if cost < distance[sink]:
                distance[sink] = cost
                previous[sink] = source
                decrease_key(queue, sink, cost)
    return distance, previous


def test_graph():
    g = sample_graph()
    print(graph_iter(g, start=1))
    print(graph_iter(g, start=1, is_bfs=False))
    print(graph_dfs_recur(g, start=1))
    assert not graph_cycle_recur(g)
    assert graph_cycle_recur(g=cycle_graph())
    assert graph_path(g, start=1, goal=5) == [1, 4, 5]


# Tree
class TreeNode(object):
    def __init__(self, v):
        self.val = v
        self.left = self.right = None

    def __str__(self) -> str:
        return str(self.val)


def preorder_recur(n: TreeNode) -> List[TreeNode]:
    res = []
    def dfs(root):
        if root: res.append(root.val)
        if root.left: dfs(root.left)
        if root.right: dfs(root.right)

    dfs(n)
    return res


def inorder_recur(n: TreeNode) -> List[TreeNode]:
    res = []
    def dfs(root):
        if root.left: dfs(root.left)
        if root: res.append(root.val)
        if root.right: dfs(root.right)

    dfs(n)
    return res


def postorder_recur(n: TreeNode) -> List[TreeNode]:
    res = []
    def dfs(root):
        if root.left: dfs(root.left)
        if root.right: dfs(root.right)
        if root: res.append(root.val)

    dfs(n)
    return res


def preorder_iter(n: TreeNode) -> List[TreeNode]:
    stk = [n]
    while stk:
        cur = stk.pop()
        yield cur.val
        if cur.right: stk.append(cur.right)
        if cur.left: stk.append(cur.left)


def inorder_iter(n: TreeNode) -> List[TreeNode]:
    stk = []
    cur = n
    while stk or cur:  # stk represents encountered nodes not yet visited
        if cur:
            stk.append(cur)  # visit left first
            cur = cur.left
        else:
            cur = stk.pop() # no left, visit current, then go right
            yield cur.val
            cur = cur.right


def postorder_iter(n: TreeNode) -> List[TreeNode]:
    stk = []
    cur = n
    last_visited = None  # avoid revisiting Node's right subtree
    while stk or cur:
        if cur:
            stk.append(cur)
            cur = cur.left
        else:
            peek = stk[-1]
            if peek.right and peek.right != last_visited:
                cur = peek.right  # if right exist and unvisited, go before cur
            else:
                last_visited = stk.pop()
                yield last_visited.val


def test_tree():
    #  1
    # / \
    # 2   3
    #   / \
    #  4*  5
    a = TreeNode(1)
    a.left = TreeNode(2)
    a.right = TreeNode(3)
    a.right.left = TreeNode(4)
    a.right.right = TreeNode(5)

    b = TreeNode(1)
    b.left = TreeNode(2)
    b.right = TreeNode(3)
    b.right.left = TreeNode(4)
    b.right.right = TreeNode(5)

    print(preorder_recur(a))
    print(list(preorder_iter(a)))

    print(inorder_recur(a))
    print(list(inorder_iter(a)))

    print(postorder_recur(a))
    print(list(postorder_iter(a)))


# test_tree()


# trie (works for hay, haywood)
class TrieNode(object):
    def __init__(self):
        self.terminal = False
        self.children = dict() # type: Dict[str, TrieNode]


def build_trie(words: List[str]) -> TrieNode:
    head = TrieNode()
    for w in words:
        cur = head
        for c in w:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.terminal = True
    return head


def trie_matches(root: TrieNode, prefix: str) -> List[str]:
    cur = root
    for c in prefix:
        if c not in cur.children:
            return []
        cur = cur.children[c]

    stk = [(cur, prefix)]
    while stk:
        cur, pref = stk.pop()
        if cur.terminal:
            yield pref
        stk.extend((child, pref + c) for c, child in cur.children.items())


# test_trie()
def test_trie():
    words = ['be', 'bear', 'bears', 'bearable', 'barney']
    root = build_trie(words)
    print(list(trie_matches(root, prefix='bear')))


# min-heap
# https://runestone.academy/runestone/books/published/pythonds/Trees/BinaryHeapImplementation.html
class BinaryHeap(object):
    def __init__(self):
        self.arr = [0]

    @property
    def size(self) -> int:
        return len(self.arr) - 1

    def from_list(self, a):
        self.arr = [0] + a[:]
        for i in range(len(a) // 2, 0, -1):
            self._sift_down(i)

    def insert(self, v):
        self.arr.append(v)
        self._sift_up(self.size)

    def _sift_up(self, i: int):
        while i // 2:
            if self.arr[i // 2] > self.arr[i]:
                self.arr[i // 2], self.arr[i] = self.arr[i], self.arr[i // 2]
            i //= 2

    def remove_min(self):
        res = self.arr[1]
        self.arr[1] = self.arr.pop()
        self._sift_down(1)
        return res

    def _sift_down(self, i: int):
        while i * 2 <= self.size:
            min_child = self._min_child(i)
            if self.arr[i] > self.arr[min_child]:
                self.arr[i], self.arr[min_child] = self.arr[min_child], self.arr[i]
            i = min_child

    def _min_child(self, i: int) -> int:
        left = i * 2
        right = i * 2 + 1
        if right > self.size:
            return left
        return left if self.arr[left] < self.arr[right] else right


# Searching
# binary search
class Search(object):
    def bin_search(self, a: List[int], val: int) -> int:
        return self._bin_search(a, left=0, right=len(a) - 1, val=val)

    def _bin_search(self, a: List[int], left: int, right: int, val: int) -> int:
        while left <= right:
            mid = (left + right) //  2
            if a[mid] == val:
                return mid
            elif a[mid] < val:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def quickselect(self, arr: List[int], k: int) -> int:
        """Find kth largest element in linear time"""
        k = len(arr) - k
        left = 0
        right = len(arr) - 1
        while left <= right:
            index = partition(arr, left, right)
            if index > k:
                right = index - 1
            elif index < k:
                left = index + 1
            else:
                return arr[index]
        return -1

def partition(a, left, right) -> int:
    pivot = a[right]
    i = left
    for j in range(left, right):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[right] = a[right], a[i]
    return i


def test_search():
    s = Search()
    a = [1, 2, 3, 4, 5, 6]
    assert s.bin_search(a, val=5) == 4
    assert s.bin_search(a, val=1) == 0
    assert s.bin_search(a, val=2) == 1
    a = [9, 5, 1, 2, 4, 0]
    assert s.quickselect(a, k=3) == 4
    assert s.quickselect(a, k=2) == 5
    assert s.quickselect(a, k=1) == 9
    assert s.quickselect(a, k=0) == -1


# test_search()


# Sorting
class Sorting(object):
    def qsort(self, a, left: int, right: int):
        if left < right:
            p = partition(a, left, right)
            self.qsort(a, left, p - 1)
            self.qsort(a, p + 1, right)

    def mergesort(self, a):
        if len(a) < 2: return
        mid = len(a) // 2
        left = a[:mid]
        right = a[mid:]
        self.mergesort(left)
        self.mergesort(right)
        i = j = k = 0
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


def test_sort():
    myList = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    Sorting().mergesort(myList)
    assert myList == [17, 20, 26, 31, 44, 54, 55, 77, 93]


test_sort()
