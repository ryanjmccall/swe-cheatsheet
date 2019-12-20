"""Recursive formulation:
for each index i, pick value v and recurse for index i + 1 with vals \ {v}
"""

def permutation(arr):
    if not arr: return []
    if len(arr) == 1: return [arr]
    res = []
    for i, v in enumerate(arr):
        res.extend([v] + p for p in permutation(arr[:i] + arr[i + 1:]))

    return res


def test():
    for perm in permutation(arr=list('1234')):
        print(''.join(perm))


test()
