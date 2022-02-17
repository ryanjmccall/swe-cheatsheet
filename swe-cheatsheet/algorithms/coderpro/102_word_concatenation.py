from typing import List


class Node(object):
    def __init__(self):
        self.terminal = False
        self.leaves = dict()

    def __repr__(self):
        return f'{self.terminal} {self.leaves}'


class TrieSolution(object):
    def __init__(self, words):
        self.words = words
        self.root = Node()
        for word in words:
            cur = self.root
            for c in word:
                if c not in cur.leaves:
                    cur.leaves[c] = Node()
                cur = cur.leaves[c]
            cur.terminal = True

    def get_concatenated_words(self) -> List[str]:
        return [w for w in self.words if self._num_substrings(w) > 1]

    def _num_substrings(self, w: str, count=0) -> int:
        for i in range(len(w)):
            pre, suf = w[:i+1], w[i+1:]
            if self.trie_contains(pre):
                subs = self._num_substrings(suf, count=count+1)
                if subs or (subs == 0 and not suf):
                    return count + subs + 1

        return 0

    def trie_contains(self, pre: str) -> bool:
        cur = self.root
        for c in pre:
            if c not in cur.leaves:
                return False
            cur = cur.leaves[c]

        return cur.terminal


test = ['cat', 'cats', 'dog', 'catsdog']
print(TrieSolution(words=test).get_concatenated_words())


class Solution(object):

    def __init__(self, words: List[str]):
        self.words = set(words)
        self.cache = dict()

    def find_concat_words(self):
        return [w for w in self.words if self._can_form(w)]

    def _can_form(self, word: str) -> bool:
        if word in self.cache:
            return self.cache[word]

        for i in range(1, len(word)):
            pre, suf = word[:i], word[i:]
            if pre in self.words:
                if suf in self.words or self._can_form(suf):
                    self.cache[word] = True
                    return True

        self.cache[word] = False
        return False


print(Solution(test).find_concat_words())

