from collections import deque
from typing import List

# Print binary tree using DFS (in-order, preorder and post order - all
#     three of them) and BFS.

class TreeNode:
    def __init__(self, v: int):
        self.val = v
        self.left = None
        self.right = None


def sampleTree() -> TreeNode:
    """
              0
        1           2
    3       5     4    6
      7   8     9        10
    """
    nodes = {v: TreeNode(v) for v in range(11)}
    nodes[0].left = nodes[1]
    nodes[0].right = nodes[2]

    nodes[1].left = nodes[3]
    nodes[1].right = nodes[5]

    nodes[2].left = nodes[4]
    nodes[2].right = nodes[6]

    nodes[3].right = nodes[7]
    nodes[5].left = nodes[8]

    nodes[4].left = nodes[9]
    nodes[6].right = nodes[10]

    return nodes[0]


def dfsPreOrder(root: TreeNode) -> List[int]:
    traversal = []
    def preOrder(t: TreeNode):
        if t:
            # root, left, right
            traversal.append(t.val)
            preOrder(t.left)
            preOrder(t.right)

    preOrder(root)
    return traversal


def dfsInOrder(root: TreeNode) -> List[int]:
    traversal = []
    def inOrder(t: TreeNode):
        if t:
            # left, root, right
            inOrder(t.left)
            traversal.append(t.val)
            inOrder(t.right)

    inOrder(root)
    return traversal


def dfsPostOrder(root: TreeNode) -> List[int]:
    traversal = []
    def inOrder(t: TreeNode):
        if t:
            # left, right, root
            inOrder(t.left)
            inOrder(t.right)
            traversal.append(t.val)


    inOrder(root)
    return traversal


def bfs(root: TreeNode) -> List[int]:
    if not root:
        return []

    q = deque([root])
    traversal = []
    while q:
        cur = q.popleft()
        traversal.append(cur.val)
        if cur.left:
            q.append(cur.left)
        if cur.right:
            q.append(cur.right)

    return traversal


def runTraversals():
    t = sampleTree()
    print("pre\t%s" % dfsPreOrder(t))
    print("in\t%s" % dfsInOrder(t))
    print("pst\t%s" % dfsPostOrder(t))
    print("bfs\t%s" % bfs(t))


runTraversals()
