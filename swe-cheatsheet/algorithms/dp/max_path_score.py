"""

Find the maximal score you can achieve by moving from the start to the end of an array
You can move at most 'maxStep' positions at any time.
The value of the array where you land is added to your score each time.

result = 10 + 2 + 5 + 20 = 37

"""

class Node:
    def __init__(self, v):
        self.val = v
        self.nxt = None
        self.prev = None


def journey(path, maxStep):
    # idea: if min val in negative, add min val to every element in path, then later substact it
    # min_val = min(path)
    # path2 = [x + min_val for x in path]
    # print(path2)

    # head = Node(v=path[-1])
    memo = [0] * len(path)
    memo[-1] = path[-1]
    for i in range(len(path) - 2, -1, -1):
        end = min(len(path) - 1, i + maxStep)
        max_val = max(memo[i + 1: end + 1])  # linear
        memo[i] = path[i] + max_val

    return memo[0]



def t():
    path = [10, 2, -10, 5, 20]
    maxStep = 2
    assert journey(path, maxStep) == 37


t()
