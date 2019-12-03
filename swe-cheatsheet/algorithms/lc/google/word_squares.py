from typing import List


def get_permutations(arr):
    if not arr: return []
    if len(arr) == 1: return [arr]
    res = []
    for i in range(len(arr)):
        v = [arr[i]]
        sub = arr[:i] + arr[i+1:]
        res.extend((v + p for p in get_permutations(arr=sub)))
    return res


class Solution(object):
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        return [perm for perm in get_permutations(words) if self.is_word_square(perm)]

    def is_word_square(self, words) -> bool:
        for i, row in enumerate(words):
            col = ''.join(r[i] for r in words)
            if row != col:
                return False

        return True


x = ["area","lead","wall","lady","ball"]
# x = ['ball', 'area', 'lead', 'lady']
print(Solution().wordSquares(x))
