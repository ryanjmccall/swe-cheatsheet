import collections

from typing import List


class Solution:
    def canFinish_(self, numCourses, prerequisites):
        # Slow recursive DFS
        graph = collections.defaultdict(list)
        for source, sink in prerequisites:
            graph[source].append(sink)

        visited = set()

        def has_cycle(vertex):
            visited.add(vertex)
            for neighbour in graph[vertex]:
                if neighbour in visited or has_cycle(neighbour):
                    return True
            visited.remove(vertex)
            return False

        for i in range(numCourses):
            if has_cycle(i):
                return False

        return True

    def canFinish(self, vertices: int, edges) -> bool:
        graph = collections.defaultdict(list)
        indegree = [0] * vertices
        for sink, source in edges:
            graph[source].append(sink)  # adj list
            indegree[sink] += 1    # count indegree

        # walk over root vertices and decrease indegree of all neighbors
        queue = [v for v, deg in enumerate(indegree) if deg == 0]
        num_roots = len(queue)
        while queue:
            v = queue.pop()
            for sink in graph[v]:
                indegree[sink] -= 1
                if indegree[sink] == 0:
                    num_roots += 1
                    queue.append(sink)

        return num_roots == vertices


print(Solution().canFinish(2, [[0, 1], [1, 0]]))



