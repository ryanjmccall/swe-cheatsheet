from typing import List


class Node:
    def __init__(self, v, l=None, r=None):
        self.v = v
        self.l = l
        self.r = r

    def __repr__(self):
        # res = str(self.v)
        # if self.l:
        #     res += str(self.l)
        # if self.r:
        #     res += str(self.r)
        # return res
        return f'{self.v}, {self.l}, {self.r}'


def to_bst(a: List[int]):
    if not a:
        return None

    mid = len(a) // 2
    root = Node(a[mid])
    root.l, root.r = to_bst(a[:mid]), to_bst(a[mid+1:])
    return root


def preorder(n: Node):
    if n:
        print(n.v)
        preorder(n.l)
        preorder(n.r)


# tree = to_bst(list(range(1, 8)))
# preorder(tree)

def gen_tree(nums):
    if not nums:
        return [None]
    if len(nums) == 1:
        return [Node(nums[0])]

    bsts = []
    for i, n in enumerate(nums):
        # lefts = gen_tree(range(nums[0], n))
        # rights = gen_tree(range(n + 1, nums[-1] + 1))
        lefts = gen_tree(nums[:i])
        rights = gen_tree(nums[i+1:])
        for left in lefts:
            for right in rights:
                bsts.append(Node(n, left, right))

    return bsts


def generate_bst(n):
    return gen_tree(range(1, n + 1))


for t in generate_bst(3):
    print(t)

