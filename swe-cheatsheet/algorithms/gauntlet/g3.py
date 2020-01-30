"""
The Gauntlet is a series of algorithms,
commonly employed by coding question solutions,
written succintly in Python.
"""
from collections import defaultdict


def sample_graph():
    # 1 > 2 > (6, 7, 8)
    # 1 > 3
    # 1 > 4 > 5
    edges = [(1, 2), (1, 3), (1, 4), (4, 5), (2, 6), (2, 7), (2, 8)]
    return get_adjacency_list(edges)


def cycle_graph():
    return get_adjacency_list(edges=[(0, 1), (1, 2), (2, 3), (3, 1)])


def get_adjacency_list(edges):
    adj = defaultdict(set)
    for u, v in edges:
        adj[u].add(v)
    return adj


# _Graph_
# bfs iter
# dfs recur
# dfs iter
# topological sort
# cycle detection (recur & top)
# dijkstra


def top_sort(g):
    indegree = defaultdict(int)
    for sinks in g.values():
        for s in sinks:
            indegree[s] += 1

    res = []
    stk = [v for v in g if not indegree[v]]
    while stk:
        cur = stk.pop()
        res.append(cur)
        for nbr in g[cur]:
            indegree[nbr] -= 1
            if not indegree[nbr]:
                stk.append(nbr)

    return [] if any(indegree.values()) else res





print(top_sort(sample_graph()))


# _Tree_
# inorder, preorder, postorder recursively
# inorder, preorder, postorder iteratively


class TreeNode:
    def __init__(self, v):
        pass


def test_tree():
    #  1
    # / \
    # 2   3
    #   / \
    #  4*  5
    a = TreeNode(1)
    a.left = TreeNode(2)
    a.right = TreeNode(3)
    a.right.left = TreeNode(4)
    a.right.right = TreeNode(5)

    b = TreeNode(1)
    b.left = TreeNode(2)
    b.right = TreeNode(3)
    b.right.left = TreeNode(4)
    b.right.right = TreeNode(5)

# trie (works for hay, haywood)

# heap

# _Sorting_
# mergesort
# quicksort

# _Searching_
# quickselect
# binary search

# permutations & combinations
