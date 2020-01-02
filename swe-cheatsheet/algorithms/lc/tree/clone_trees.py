from typing import Optional


class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def find_node(root1: Node, root2: Node, target: Node) -> Optional[Node]:
    stk = [(root1, root2)]
    while stk:
        a, b = stk.pop()
        if a == target:
            return b

        if a.right and b.right:
            stk.append((a.right, b.right))
        if a.left and b.left:
            stk.append((a.left, b.left))

    return None



def t():
    #  1
    # / \
    #2   3
    #   / \
    #  4*  5
    a = Node(1)
    a.left = Node(2)
    a.right = Node(3)
    a.right.left = Node(4)
    a.right.right = Node(5)

    b = Node(1)
    b.left = Node(2)
    b.right = Node(3)
    b.right.left = Node(4)
    b.right.right = Node(5)

    print(find_node(a, b, a.right.left).val)
    # 4


t()
