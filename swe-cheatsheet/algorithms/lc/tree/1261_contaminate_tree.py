class FindElements:

    def __init__(self, root):
        self._values = set()
        if not root:
            return

        def dfs(node, v: int):
            node.val = v
            self._values.add(v)
            if node.left:
                dfs(node.left, 2 * node.val + 1)
            if node.right:
                dfs(node.right, 2 * node.val + 2)

        dfs(root, 0)

    def find(self, target: int) -> bool:
        return target in self._values

#         stack = [self.root]
#         while stack:
#             current = stack.pop()
#             if current.right:
#                 current.right.val = 2 * current.val + 2
#                 self._values.add(current.right.val)
#                 stack.append(current.right)
#
#             if current.left:
#                 current.left.val = 2 * current.val + 1
#                 self._values.add(current.left.val)
#                 stack.append(current.left)
