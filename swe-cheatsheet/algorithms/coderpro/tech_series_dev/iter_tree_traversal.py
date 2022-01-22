class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder_iter(root: Node):
    current = root
    stack = []
    while current or stack:
        if current:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            print(current.val)
            current = current.right


def test():
    n = Node(0)
    n.left = Node(1)
    n.right = Node(2)
    n.left.left = Node(3)
    n.left.right = Node(4)
    n.right.left = Node(5)
    n.right.right = Node(6)
    inorder_iter(n)


test()
