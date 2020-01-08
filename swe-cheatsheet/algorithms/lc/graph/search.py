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

    def dfs_path(self, g, start, goal):
        if not start: return []
        stk = [(start, [start])]
        visited = set()
        while stk:
            cur, path = stk.pop()
            if cur == goal:
                return path
            visited.add(cur)
            for n in g[cur] - visited:
                stk.append((n, path + [n]))

        return []


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
    # print(s.dfs(g, 1))
    # print(s.bfs(g, 1))
    print(s.dfs_path(g, 1, 8))
    print(s.dfs_path(g, 8, 8))
    print(s.dfs_path(g, 8, 5))
    print(s.dfs_path(g, 1, 55))


t()
