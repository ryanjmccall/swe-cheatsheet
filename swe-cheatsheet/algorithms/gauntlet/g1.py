# Mon Jan 6th, 2019
# Time taken: 5:46pm
# Hints taken:

from typing import List, Set, Dict, Tuple

from collections import defaultdict, deque


# Graph
def get_adjacency_list(edges: List[Tuple[int, int]]) -> Dict[int, Set[int]]:
    g = defaultdict(set)
    for u, v in edges:
        g[u].add(v)
    return g


def sample_graph():
    edges = [(1, 2), (1, 3), (1, 4), (4, 5), (2, 6), (2, 7), (2, 8)]
    return get_adjacency_list(edges)


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


def has_cycle_recur(g) -> bool:
    pass  # actually return the cycle this time

# - dijkstra

# Tree
# - inorder, preorder, postorder recursively
# - inorder, preorder, postorder iteratively

# - trie (works for hay, haywood)

# - heap

# Sorting
# - mergesort
# - quicksort

# Searching
# - quickselect
# - binary search

def t():
    print(graph_iter(sample_graph(), start=1))
    print(graph_iter(sample_graph(), start=1, is_bfs=False))
    print(graph_dfs_recur(sample_graph(), start=1))


t()
