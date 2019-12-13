class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

def valuesAtLevel_my_recur(node, depth):
    res = []

    def dfs(n, d):
        if not n: return
        if d == depth:
            res.append(n.value)
            return

        dfs(n.left, d + 1)
        dfs(n.right, d + 1)

    dfs(node, 1)
    return res


def valuesAtLevel_iter(node, depth):
    res = []
    stk = [(node, 1)] if node else []
    while stk:
        cur, d = stk.pop()
        if d == depth:
            res.append(cur.value)
            continue

        if cur.right:
            stk.append((cur.right, d+1))
        if cur.left:
            stk.append((cur.left, d+1))

    return res

def values_recur(node, depth):
    if not node: return []
    if depth == 1: return [node.value]
    return values_recur(node.left, depth - 1) + values_recur(node.right, depth - 1)


#    1
#   / \
#  2   3
# / \   \
# 4   5   7
def test():
    node = Node(1)
    node.left = Node(2)
    node.right = Node(3)
    node.right.right = Node(7)
    node.left.left = Node(4)
    node.left.right = Node(5)

    print(valuesAtLevel_iter(node, 3))
    print(values_recur(node, 3))
    print(valuesAtLevel_my_recur(node, 3))

test()
