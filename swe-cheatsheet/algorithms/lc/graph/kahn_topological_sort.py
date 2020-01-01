from collections import defaultdict
from typing import List, Tuple

"""
Kahn's topological sort
Input: V vertices, E edges
Space: O(V + E), constant on V is 3
Time: O(V + E), constant on V is 4
LOC: 21
"""

def top_sort(edges: List[Tuple[int, int]]) -> List[int]:
    adj = defaultdict(set)
    indegree = defaultdict(int)
    for u, v in edges:
        adj[u].add(v)
        indegree[v] += 1

    res = []
    stack = [n for n in adj if indegree[n] == 0]
    while stack:
        cur = stack.pop()
        res.append(cur)
        for nbr in adj[cur]:
            indegree[nbr] -= 1
            if indegree[nbr] == 0:
                stack.append(nbr)

    return [] if any(v for v in indegree.values()) else res


def has_cycle_iter(edges, start: int):
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)

    visited = set()
    stk = [start]
    while stk:
        cur = stk.pop()
        if cur in visited:
            return True
        visited.add(cur)
        stk.extend(adj[cur])
    return False


def example_edges():
    return [(1, 3), (3, 4), (4, 5), (2, 4), (5, 6), (9, 3), (10, 20)]


def test():
    edges = example_edges()
    assert top_sort(edges) == [10, 20, 9, 2, 1, 3, 4, 5, 6]

    edges = cycle_edges()
    assert top_sort(edges) == []

def cycle_edges():
    return [(1, 2), (2, 3), (3, 1)]

def test_dfs():
    edges = cycle_edges()
    assert has_cycle_iter(edges, start=1)

    edges = example_edges()
    assert not has_cycle_iter(edges, start=1)


# test()
test_dfs()
