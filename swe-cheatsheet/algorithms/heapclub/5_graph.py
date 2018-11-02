#!/usr/bin/env python
from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.adjacencyList = defaultdict(set)

    def addVertex(self, v: str) -> set:
        """Adds vertex v and returns any existing neighbors"""
        return self.adjacencyList[v]

    def addEdge(self, a: str, b: str):
        self.adjacencyList[a].add(b)

    def bfs(self, n: str) -> list:
        if n not in self.adjacencyList:
            return []

        order = []
        visited = set()
        q = deque([n])
        while q:
            c = q.popleft()
            if c not in visited:
                visited.add(c)
                order.append(c)
                q.extend(self.adjacencyList[c])

        return order

    def dfs(self, n: str) -> list:
        if n not in self.adjacencyList:
            return []

        order = []
        visited = set()
        stack = [n]
        while stack:
            c = stack.pop()
            visited.add(c)
            order.append(c)
            stack.extend(filter(lambda k: k not in visited,
                                self.adjacencyList[c]))

        return order


def main():
    g = Graph()
    g.addEdge("a", "b")
    g.addEdge("b", "c")
    g.addEdge("c", "a")

    g.addEdge("b", "y")
    g.addEdge("y", "z")

    #     a
    #     b
    #  c       y
    #  a*        z

    # expect a, b, [c, y], z
    print(g.bfs("a"))

    # expect one of:
    # a, b, c, y, z
    # a, b, y, z, c
    print(g.dfs("a"))

if __name__ == "__main__":
    main()
