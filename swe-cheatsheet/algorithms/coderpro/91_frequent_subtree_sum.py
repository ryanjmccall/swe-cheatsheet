from collections import defaultdict, Counter


class Node:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def frequent_sum(n: Node) -> int:
    sums = defaultdict(int)

    def dfs(r):
        if not r:
            return 0
        lsum = dfs(r.left)
        rsum = dfs(r.right)
        total = r.val + lsum + rsum
        sums[total] += 1
        return total

    dfs(n)
    return max(sums.items(), key=lambda x: x[1])[0] if sums else 0


# def frequent_sum(n: Node) -> int:
#     def dfs(r):
#         if not r: yield 0
#         yield r.val + dfs(r.left) + dfs(r.right)
#     return Counter(dfs(n)).most_common(1)[0][0]


root = Node(3, Node(-3), Node(1))
print(frequent_sum(root))

