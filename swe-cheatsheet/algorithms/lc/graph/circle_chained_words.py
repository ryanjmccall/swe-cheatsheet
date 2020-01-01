from typing import List, Dict
from collections import defaultdict


def is_chained_(words: List[str]) -> bool:
    edges = []
    for w in words:
        edges.append((w[0], w[-1]))
        edges.append((w[-1], w[0]))

    return top_sort(edges) == []


def top_sort(edges) -> list:
    adj = defaultdict(set)
    indegree = defaultdict(int)
    for u, v in edges:
        adj[u].add(v)
        indegree[v] += 1

    res = []
    stk = [n for n, count in indegree.items() if count == 1]
    while stk:
        cur = stk.pop()
        res.append(cur)
        for nbr in adj[cur]:
            indegree[nbr] -= 1
            if indegree[nbr] == 0:
                stk.append(nbr)

    return list() if any(count for count in indegree.values()) else res


def is_chained(words):
    symbol = defaultdict(list)
    for w in words:
        symbol[w[0]].append(w)

    start = words[0]
    visited = set()
    def is_cycle_dfs(current: str, length: int) -> bool:
        if length == 1:
            return start[0] == current[-1]

        visited.add(current)
        for n in symbol[current[-1]]:
            if n not in visited:
                return is_cycle_dfs(n, length - 1)

        visited.remove(current)
        return False


    return is_cycle_dfs(current=words[0], length=len(words))


print(is_chained(words=['apple', 'eggs', 'snack', 'karat', 'tuna']))
print(is_chained(words=['apple', 'eggs', 'snack', 'karat', 'tunax']))

