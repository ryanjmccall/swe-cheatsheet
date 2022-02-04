"""
The Gauntlet is a set of coding tasks for algorithms commonly used in coding question solutions
written succintly in Python.
"""

from typing import List


### Section 0. Linked List

# define datastructure

# create

# traverse

# prepend

# append

# insert

# remove

### Section 1. Graph algorithms


def get_adjacency_list(edges):
    # TODO: given a set of edges construct a graph
    pass


def sample_dag() -> List[tuple]:
    """
    1 > 2 > (6, 7, 8)
    1 > 3
    1 > 4 > 5
    """
    edges = [(1, 2), (1, 3), (1, 4), (4, 5), (2, 6), (2, 7), (2, 8)]
    return get_adjacency_list(edges)


def sample_dcg():
    """ 0 > 1 > 2 > 3 > 1  """
    return get_adjacency_list(edges=[(0, 1), (1, 2), (2, 3), (3, 1)])


# bfs iter

# dfs recur

# dfs iter

# topological sort

# cycle detection using recursion

# cycle detection using top sort

# graph path to value

# dijkstra's algo


### Section 2. Tree algorithms

# TODO create the fundamental tree datastructure

def sample_tree():
    #  1
    # / \
    # 2   3
    #   / \
    #  4*  5
    # a = Node(1)
    # a.left = Node(2)
    # a.right = Node(3)
    # a.right.left = Node(4)
    # a.right.right = Node(5)
    #
    # b = Node(1)
    # b.left = Node(2)
    # b.right = Node(3)
    # b.right.left = Node(4)
    # b.right.right = Node(5)
    pass

# what is preorder?

# what is inorder?

# what is postorder?

# inorder recur

# preorder recur

# postorder recur

# inorder iter

# preorder iter

# postorder iter

### Section 3. Retrieval tree / trie
# must work for 'hi' and 'higher'

# code build_trie

# code match_trie

### Section 4. Binary heap
# methods: insert, remove_min


### Section 5. Searching
# quickselect

# binary search

# print(binary_search([1, 1, 1, 1, 2, 3, 4, 5, 5], 4))

### Section 6. Sorting

# mergesort

# partition

# quicksort

def test_sort():
    myList = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # TODO
    assert myList == [17, 20, 26, 31, 44, 54, 55, 77, 93]

### Section 7. Ordered Dict / LRU cache

# implement LRU cache using ordered dict

# implement ordered dict using dict

### Section 8. combinatorics

# permutation recur

# permutation iter


def test_permutations():
    vals = [3, 4, 5]

# combination recur

# combination iter


def test_combos():
    vals = list('1234')
