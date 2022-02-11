
class Node:
    def __init__(self, v: int, l=None, r=None):
        self.v = v
        self.left = l
        self.right = r


def is_balanced(root: Node) -> int:

    def dfs(n) -> int:
        if not n:
            return 0

        rheight = dfs(n.right)
        if rheight == -1:
            return -1

        lheight = dfs(n.left)
        if lheight == -1:
            return -1

        if abs(rheight - lheight) > 1:
            return -1

        return max(lheight, rheight) + 1

    return dfs(root) != -1


print(is_balanced(Node(1, l=Node(2, l=Node(4)), r=Node(3))))


print(is_balanced(Node(1, l=Node(2, l=Node(4)))))




