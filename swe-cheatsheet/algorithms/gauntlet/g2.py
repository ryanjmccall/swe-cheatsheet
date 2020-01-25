from collections import defaultdict, deque

# _Graph_
from typing import List, Iterable, Optional, Dict


def sample_graph():
    # 1 > 2 > (6, 7, 8)
    # 1 > 3
    # 1 > 4 > 5
    edges = [(1, 2), (1, 3), (1, 4), (4, 5), (2, 6), (2, 7), (2, 8)]
    return get_adjacency_list(edges)


def cycle_graph():
    return get_adjacency_list(edges=[(0, 1), (1, 2), (2, 3), (3, 1)])


def get_adjacency_list(edges) -> dict:
    g = defaultdict(set)
    for a, b in edges:
        g[a].add(b)
    return g


def graph_iter(g: dict, start: int, is_bfs: bool) -> List[int]:
    assert start in g
    visited = set()
    q = deque([start])
    while q:
        cur = q.popleft() if is_bfs else q.pop()
        visited.add(cur)
        yield cur
        q.extend(n for n in g[cur] - visited)


# print(list(graph_iter(sample_graph(), start=1, is_bfs=True)))
# print(list(graph_iter(sample_graph(), start=1, is_bfs=False)))


# dfs recur
def graph_recur(g: dict, start: int) -> Iterable[int]:
    res = []
    _dfs(g, start, res, visited=set())
    return res


def _dfs(g, n, res, visited: set):
    res.append(n)
    visited.add(n)
    for nbr in g[n] - visited:
        _dfs(g, nbr, res, visited)



# print(list(graph_recur(sample_graph(), start=1)))


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

    return [] if any(cnt for cnt in indegree.values()) else res


# print(top_sort(sample_graph()))
# print(top_sort(cycle_graph()))


# cycle detection (recur & top)
def has_cycle(g) -> bool:
    return not top_sort(g)


def has_cycle_recur(g) -> bool:
    visited = set()
    for v in g:
        if v not in visited and _dfs_cycle(g, v, visited):
            return True
    return False


def _dfs_cycle(g, n: int, visited: set) -> bool:
    visited.add(n)
    for nbr in g[n]:
        if nbr in visited or _dfs_cycle(g, n, visited):
            return True
    visited.remove(n)
    return False


def graph_path(g, start: int, goal: int) -> Optional[List[int]]:
    visited = set()
    def dfs(node: int, path: List[int]) -> Optional[List[int]]:
        visited.add(node)
        path.append(node)
        if node == goal:
            return path

        for nbr in g[node] - visited:
            res = dfs(nbr, path)
            if res is not None:
                return res

        visited.remove(node)
        path.pop()
        return None

    return dfs(start, [])


# dijkstra
def extract_min(q): return 0
def decrease_key(q, k, v): pass

def dijkstra_shortest_paths(g, start: int):
    distance = {v: float('inf') for v in g}
    distance[start] = 0
    previous = {v: None for v in g}
    q = list(g)
    while q:
        source = extract_min(q)
        for sink, weight in g[source]:
            cost = distance[source] + weight
            if cost < distance[sink]:
                distance[sink] = cost
                previous[sink] = source
                decrease_key(q, sink, cost)
    return distance, previous


# _Tree_
class TreeNode(object):
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None


# preorder, inorder, postorder recursively
def preorder_recur(n: TreeNode) -> Iterable[TreeNode]:
    if not n: return
    yield n.val
    if n.left:
        yield from preorder_recur(n.left)
    if n.right:
        yield from preorder_recur(n.right)


def inorder_recur(n: TreeNode) -> Iterable[TreeNode]:
    if not n: return
    if n.left:
        yield from preorder_recur(n.left)
    yield n.val
    if n.right:
        yield from preorder_recur(n.right)


def postorder_recur(n: TreeNode) -> List[TreeNode]:
    if not n: return
    if n.left:
        yield from preorder_recur(n.left)
    if n.right:
        yield from preorder_recur(n.right)
    yield n.val


def preorder_iter(n: TreeNode) -> Iterable[TreeNode]:
    stk = [n]
    while stk:
        cur = stk.pop()
        yield cur.val
        if cur.right: stk.append(cur.right)
        if cur.left: stk.append(cur.left)


def inorder_iter(n: TreeNode) -> Iterable[TreeNode]:
    stk = []
    cur = n
    while stk or cur:  # stk nodes skipped to be visited later
        if cur:
            stk.append(cur)
            cur = cur.left
        else:
            cur = stk.pop()
            yield cur.val
            cur = cur.right


# preorder, inorder, postorder iteratively
def postorder_iter(n: TreeNode) -> Iterable[TreeNode]:
    stk = []
    cur = n
    last_visited = None
    while stk or cur:
        if cur:
            stk.append(cur)
            cur = cur.left
        else:
            peek = stk[-1]
            if peek.right and peek.right != last_visited:
                cur = peek.right
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

    print(list(preorder_recur(a)))


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
        cur, pre = stk.pop()
        if cur.terminal:
            yield pre
        stk.extend((child, pre + c) for c, child in cur.children.items())

# heap
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


# _Searching_
# quickselect unsorted array
def quickselect(a: List[int], target: int) -> int:
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


# binary search sorted array
def binary_search(a: List[int], target: int) -> int:
    left = 0
    right = len(a) - 1
    while left < right:
        mid = (left + right) // 2
        val = a[mid]
        if val < target:
            left = mid + 1
        elif val > target:
            right = mid - 1
        else:
            return mid

    return -1


# print(binary_search([1, 1, 1, 1, 2, 3, 4, 5, 5], 4))


def partition(a, left, right) -> int:
    pivot = a[right]
    i = left
    for j in range(left, right):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[right] = a[right], a[i]
    return i


# _Sorting_
# mergesort
# quicksort
class Sorting(object):
    def qsort(self, a, left: int, right: int):
        if left < right:
            p = partition(a, left, right)
            self.qsort(a, left, p - 1)
            self.qsort(a, p + 1, right)

    def mergesort(self, a):
        if len(a) <= 1: return
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


class Permutation:
    # idea given left (completed), right (pending), how to add from right?
    # loop over right and gen all possibilities
    def permute_recur(self, vals):
        if not vals: return []
        res = []

        def dfs(left, right):
            if not right:
                res.append(left)
                return

            for i, v in enumerate(right):  # for each v, maintain everything else in the right
                dfs(left=left + [v], right=right[:i] + right[i+1:])

        dfs(left=[], right=vals)
        return res

    def permute_iter(self, vals):
        if not vals: return []
        stack = [([], vals)]
        for left, right in stack:
            for i, v in enumerate(right):
                remain = right[:i] + right[i + 1:]
                if remain:
                    stack.append((left + [v], remain))
                else:
                    yield left + [v]

class Combination:
    def combos_recur_gen(self, left: list, right: list):
        for i, v in enumerate(right):
            yield left + [v]
            yield from self.combos_recur_gen(left + [v], right[i + 1:])

    def combos_iter_gen(self, vals):  # This is amazing
        stack = [([], vals)]
        for left, right in stack:
            for i, v in enumerate(right):
                yield left + [v]
                stack.append((left + [v], right[i + 1:]))

def t():
    combo = Combination()
    # res = combo.combos_recur_gen(left=[], right=list('1234'))
    # print('\n'.join(''.join(c) for c in res))
    print()
    res = combo.combos_iter_gen(vals=list('1234'))
    print('\n'.join(''.join(c) for c in res))


t()


# print(Permutation().permute_recur(vals=[3, 4, 5]))
print(list(Permutation().permute_iter(vals=[3, 2])))
