class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    OPS = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y
    }

    def eval_tree(self, n: Node) -> int:
        if not n:
            return 0

        if isinstance(n.val, int):
            return n.val

        if n.val not in self.OPS:
            raise ValueError('bad op ' + n.val)

        left = self.eval_tree(n.left)
        right = self.eval_tree(n.right)
        return self.OPS[n.val](left, right)


tree = Node('*', Node('+', Node(3), Node(2)), Node('+', Node(4), Node(5)))
print(Solution().eval_tree(tree))
