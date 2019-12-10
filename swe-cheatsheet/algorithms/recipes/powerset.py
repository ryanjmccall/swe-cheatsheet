#!/usr/bin/env python
from itertools import chain, combinations


def powerset(iterable):
    # powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

# Output:

# >>> list(powerset("abcd"))
# [(), ('a',), ('b',), ('c',), ('d',), ('a', 'b'), ('a', 'c'), ('a', 'd'),
# ('b', 'c'), ('b', 'd'), ('c', 'd'), ('a', 'b', 'c'), ('a', 'b', 'd'),
# ('a', 'c', 'd'), ('b', 'c', 'd'), ('a', 'b', 'c', 'd')]

# If you don't like that empty tuple at the beginning, you can just change the
# range statement to range(1, len(s)+1) to avoid a 0-length combination.
