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


class Solution1(object):
    def wordSquares1(self, words: List[str]) -> List[List[str]]:
        return [perm for perm in get_permutations(words) if self.is_word_square(perm)]

    def is_word_square(self, words) -> bool:
        for i, row in enumerate(words):
            col = ''.join(r[i] for r in words)
            if row != col:
                return False

        return True

    def wordSquares(self, words):
        if not words: return []
        self.words = words
        self.n = len(words[0])
        res = []
        for w in words:
            self.dfs(index=1, square=[w], results=res)
        return res

    def dfs(self, index, square, results):
        if index == self.n:
            results.append(square[:])
            return

        pre = ''.join(w[index] for w in square)  # TODO can't this be passed in?
        for w in self._words_starting_with(pre):
            square.append(w)
            self.dfs(index + 1, square, results)
            square.pop()

    def _words_starting_with(self, prefix):
        return [w for w in self.words if w.startswith(prefix)]


# x = ["area","lead","wall","lady","ball"]
x = ['area', 'lead', 'ball', 'lady']
print(Solution1().wordSquares(x))
