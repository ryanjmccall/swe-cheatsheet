# Problem:
# Given various subsequences of an array of unique integers, return the original array:
#
# Input: [1, 3, 5], [1, 3, 9], [9, 5], ....,
# Output : [1, 3, 9, 5]
#
# (each subarray was generated from original by deleting items/preserving order)
#
# Solution: This is a graph problem disguised as an array problem. Most easily solved by topological sort
from collections import defaultdict
from typing import List


class Solution(object):

    def get_original_array(self, arrays: List[List[int]]) -> List[int]:
        # Solution by Kahn's topological sorting algorithm
        if not arrays: return []
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        for arr in arrays:
            for i in range(len(arr) - 1):
                u, v = arr[i], arr[i + 1]
                graph[u].append(v)
                in_degree[v] += 1

        res = []
        q = [n for n in graph if not in_degree[n]]
        while q:
            n = q.pop()
            res.append(n)  # remove n and decrease neighbors in-degree
            for nbr in graph[n]:
                in_degree[nbr] -= 1
                if not in_degree[nbr]:
                    q.append(nbr)

        if any(v for v in in_degree.values()):
            return []

        return res


print(Solution().get_original_array([[1, 3, 5], [1, 3, 9], [9, 5]]))
