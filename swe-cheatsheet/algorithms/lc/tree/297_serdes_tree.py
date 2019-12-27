from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        result = str(self.val)
        if self.left:
            result += str(self.left)
        if self.right:
            result += str(self.right)
        return result


class Codec:

    def serialize(self, root) -> str:
        def bfs():
            q = deque([root])
            while q:
                cur = q.popleft()
                if cur: q.extend((cur.left, cur.right))
                yield str(cur.val) if cur else ''

        return ','.join(bfs())

    def deserialize(self, data):
        if not data: return None
        vals = data.split(',')
        root = TreeNode(int(vals[0]))
        idx = 1
        q = [root]
        for n in q:
            if vals[idx]:
                n.left = TreeNode(int(vals[idx]))
                q.append(n.left)
            idx += 1

            if vals[idx]:
                n.right = TreeNode(int(vals[idx]))
                q.append(n.right)
            idx += 1

        return root


def t():
    c = Codec()
    tree = TreeNode(1)
    tree.left = TreeNode(3)
    tree.right = TreeNode(4)
    tree.left.left = TreeNode(2)
    tree.left.right = TreeNode(5)
    tree.right.right = TreeNode(7)
    string = c.serialize(tree)
    print(c.deserialize(string))

    print(c.serialize(None))


t()
