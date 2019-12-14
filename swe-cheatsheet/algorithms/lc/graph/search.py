from collections import defaultdict, deque
from typing import Set, Dict


class Search(object):
    def dfs(self, g: Dict[int, Set[int]], start: int):
        order = []
        visited = set()
        stk = [start]
        while stk:
            cur = stk.pop()
            if cur not in visited:
                order.append(cur)
                visited.add(cur)
                stk.extend(g[cur] - visited)

        return order

    def bfs(self, g: Dict[int, Set[int]], start: int):
        order = []
        visited = set()
        q = deque([start])
        while q:
            cur = q.popleft()
            if cur not in visited:
                order.append(cur)
                visited.add(cur)
                q.extend(g[cur] - visited)

        return order

    def dfs_paths(self, g, start, goal):
        stack = [(start, [start])]
        visited = set()
        while stack:
            (vertex, path) = stack.pop()
            if vertex not in visited:
                if vertex == goal:
                    return path
                visited.add(vertex)
                for n in g[vertex] - visited:
                    stack.append((n, path + [n]))

def t():
    #        1
    #    2   3   4
    #  5    6  7
    # 8
    g = defaultdict(set)
    g[1].update({2, 3, 4})
    g[2].update({5, 6})
    g[3].add(7)
    g[5].add(8)
    g[8].add(1)

    s = Search()
    print(s.dfs(g, 1))
    print(s.bfs(g, 1))
    print(next(s.dfs_paths(g, 1, 8)))


t()
