from collections import defaultdict, deque

# _Graph_
from typing import List, Iterable


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


print(list(graph_iter(sample_graph(), start=1, is_bfs=True)))
print(list(graph_iter(sample_graph(), start=1, is_bfs=False)))


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



print(list(graph_recur(sample_graph(), start=1)))



# topological sort
# cycle detection (recur & top)
# dijkstra

# _Tree_
# inorder, preorder, postorder recursively
# inorder, preorder, postorder iteratively

# trie (works for hay, haywood)

# heap

# _Sorting_
# mergesort
# quicksort

# _Searching_
# quickselect
# binary search

