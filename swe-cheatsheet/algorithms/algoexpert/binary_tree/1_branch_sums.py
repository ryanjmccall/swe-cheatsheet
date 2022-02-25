# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    sums = []

    def dfs(n, total):
        if not n:
            return

        total += n.value
        dfs(n.left, total)
        dfs(n.right, total)
        if not n.left and not n.right:
            sums.append(total)

    dfs(root, 0)
    return sums

# def branchSums(root):
#     sums = []
# 	stk = [(root, 0)]
# 	for n, total in stk:
# 		total += n.value
# 		if n.left:
# 			stk.append((n.left, total))
# 		if n.right:
# 			stk.append((n.right, total))

# 		if not n.left and not n.right:
# 			sums.append(total)

# 	return sums
