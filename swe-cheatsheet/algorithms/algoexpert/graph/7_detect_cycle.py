from typing import List


def cycleInGraph(edges: List[List[int]]) -> bool:
    """
    Time: O(|n| + |e|)
    Space: O(|n|)
    """
    path = set()
    visited = set()

    def dfs(n: int) -> bool:
        if n in path:
            return True

        path.add(n)
        visited.add(n)
        if any(dfs(v) for v in edges[n]):
            return True

        path.remove(n)
        return False

    return any(dfs(i)
               for i in range(len(edges))
               if i not in visited)
