from collections import defaultdict
from typing import List, Iterator


def sampleGraph() -> List[List[int]]:
    # A -> B, C  and B -> C
    return [
        [0, 1, 1],
        [0, 0, 1],
        [0, 0, 0]
    ]


def dfs(g, root: int):
    visited = [False] * len(g)
    def _dfs(node: int):
        print(node)
        visited[node] = True
        for i, v in enumerate(g[node]):
            if v and not visited[i]:
                _dfs(i)

    _dfs(root)


from collections import deque
def bfs(g, root: int):
    visited = [False] * len(g)
    q = deque([root])
    while q:
        cur = q.popleft()
        if not visited[cur]:
            print(cur)
            visited[cur] = True
            q.extend((i
                      for i, v in enumerate(g[cur])
                      if v and not visited[i]))


def outNeighbors(g, n: int) -> Iterator[int, None, None]:
    return (i for i, v in enumerate(g[n]) if v)


def inNeighbors(g, n: int) -> Iterator[int, None, None]:
    return (i for i, row in enumerate(g) if row[n])


def connectedComponents(g) -> List[set]:
    """Return list of strongly connected components."""
    visited = set()  # Set of visited nodes.
    L = []  # Nodes in topological order.
    def visit(u):
        if u not in visited:
            visited.add(u)
            for v in outNeighbors(g, u):
                visit(v)
            L.insert(0, u)

    for n in range(len(g)):
        visit(n)

    component = defaultdict(set)  # Map from root to its component.
    assigned = set()       # Set of nodes assigned to a component.
    def assign(u, root):
        if u not in assigned:
            component[root].add(u)
            assigned.add(u)
            for v in inNeighbors(g, u):
                assign(v, root)

    for n in L:
        assign(n, n)

    return list(component.values())


def containsCycle(g) -> bool:
    return any(len(cc) > 1 for cc in connectedComponents(g))


def run():
    print("dfs")
    dfs(sampleGraph(), 0)
    print("bfs")
    bfs(sampleGraph(), 0)


if __name__ == "__main__":
    run()
