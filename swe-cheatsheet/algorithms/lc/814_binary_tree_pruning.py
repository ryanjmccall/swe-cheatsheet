# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        left = self.left.val if self.left else None
        right = self.right.val if self.right else None
        return f'{left} < {self.val} > {right}'


def visit(node):
    print(node.val)


def preorder(node):
    if not node:
        return
    visit(node)
    preorder(node.left)
    preorder(node.right)


def preorder_iter(root):
    if not root:
        return

    stack = [root]
    while stack:
        node = stack.pop()
        print(node.value)  # visit
        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)


def inorder(node: TreeNode):
    if not node:
        return
    inorder(node)
    visit(node)
    inorder(node.right)


def inorder_iter(root: TreeNode):
    stack = []
    node = root
    while node or stack:
        # stack initially empty but current non-empty
        # current can become empty at ends of tree and stack still populated
        if node:
            # suspend current to go left first
            stack.append(node)
            node = node.left
        else:
            # leftmost does not exist, so visit current node, then go right
            node = stack.pop()
            visit(node)
            node = node.right


def postorder(node):
    if not node:
        return
    postorder(node.left)
    postorder(node.right)
    visit(node)


def postorder_iter(root: TreeNode):
    stack = []
    node = root
    # to avoid revisiting node's right subtree
    last_visited = None
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            # left exhausted, check right
            peek = stack[-1]
            if peek.right and last_visited != peek.right:
                # advance to right
                node = peek.right
            else:
                # finally visit current node
                visit(peek)
                last_visited = stack.pop()


def create_tree():
    """            5
            3               7
        2       4       6       8
    """
    root = TreeNode(5)

    root.left = TreeNode(3)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)

    root.right = TreeNode(7)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)
    return root


inorder_iter(create_tree())



class Solution:
    def pruneTree(self, root: TreeNode) -> Optional[TreeNode]:
        if root is None:
            return None

        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.left or root.right or root.val:
            return root

        return None
