# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class CBTInserter:

    def __init__(self, root: TreeNode):
        self.nodes = [root]
        for n in self.nodes:  # using iterate and modify
            if n.left:
                self.nodes.append(n.left)
            if n.right:
                self.nodes.append(n.right)

    def insert(self, v: int) -> int:
        count = len(self.nodes)
        n = TreeNode(v)
        self.nodes.append(n)

        # for complete binary tree: num_left_nodes = num_other_nodes + 1
        parent = self.nodes[(count - 1) // 2]
        if parent.left:
            parent.right = n
        else:
            parent.left = n

        return parent.val

    def get_root(self) -> TreeNode:
        return self.nodes[0] if self.nodes else None

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()