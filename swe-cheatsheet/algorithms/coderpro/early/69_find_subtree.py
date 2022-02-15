
from dataclasses import dataclass


@dataclass
class Node:
    value: int
    left = None
    right = None


n = Node(1)
n.left = Node(4)
n.right = Node(5)
n.left.left = Node(3)
n.left.right = Node(2)
n.right.left = Node(4)
n.right.right = Node(1)

b = Node(4)
b.left = Node(3)
b.right = Node(2)


def pre(n):
    if not n:
        return 'null'
    return '-'.join((str(n.value), pre(n.left), pre(n.right)))


def find_subtree(a, b):
    return pre(b) in pre(a)


print(find_subtree(n, b))


def contains_subtree(a, b) -> bool:
    if a is None and b is None:
        return True

    if not a or not b:
        return False

    if a.value == b.value and contains_subtree(a.left, b.left) and contains_subtree(a.right, b.right):
        return True

    return contains_subtree(a.left, b) or contains_subtree(a.right, b)


print(contains_subtree(n, b))
