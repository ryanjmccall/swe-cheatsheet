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
    graph = defaultdict(list)
    indegree = defaultdict(int)
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    res = []
    stack = [n for n in graph if indegree[n] == 0]
    while stack:
        cur = stack.pop()
        res.append(cur)
        for nbr in graph[cur]:
            indegree[nbr] -= 1
            if indegree[nbr] == 0:
                stack.append(nbr)

    if any(v for v in indegree.values()):
        return []

    return res


def test():
    edges = [(1, 3), (3, 4), (4, 5), (2, 4), (5, 6), (9, 3), (10, 20)]
    assert top_sort(edges) == [10, 20, 9, 2, 1, 3, 4, 5, 6]

    edges = [(1, 2), (2, 3), (3, 1)]
    assert top_sort(edges) == []


test()
