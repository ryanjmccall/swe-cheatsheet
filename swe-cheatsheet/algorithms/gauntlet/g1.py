# Mon Jan 6th, 2019

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

    return any(dfs(v) for v in g)


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


def test_trie():
    words = ['be', 'bear', 'bears', 'bearable', 'barney']
    root = build_trie(words)
    print(list(trie_matches(root, prefix='bear')))


test_trie()


# - heap

# Sorting
# - mergesort
# - quicksort

# Searching
# - quickselect
# - binary search
