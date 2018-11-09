from collections import deque
from typing import List, Union


_END = "__end__"


class Trie:
    def __init__(self, *words):
        self.root = dict()
        for w in words:
            self._insert(self.root, w)

    @staticmethod
    def _insert(node: dict, word: str):
        for c in word:
            if c not in node:
                node[c] = dict()

            node = node[c]

        node[_END] = None

    def insert(self, word: str):
        self._insert(self.root, word)

    def delete(self, word: str) -> bool:
        cur = self.root
        path = []
        for c in word:
            if c in cur:
                path.append(cur)
                cur = cur[c]
            else:
                return False

        if _END in cur:
            cur.pop(_END)
            for i in range(len(path) - 1, -1, -1):
                # work back up path removing single entry dicts
                node = path[i]
                char = word[i]
                if not node[char]:
                    del node[char]

            return True

        return False

    def contains(self, word: str) -> bool:
        # can have case where "roommate" in trie but not "room"
        ptr = self._traverse(word)
        return _END in ptr if ptr else False

    def is_prefix(self, word: str) -> bool:
        return self._traverse(word) is not None

    def words_with_prefix(self, prefix: str) -> List[str]:
        words = []
        ptr = self._traverse(prefix)
        q = deque([(ptr, prefix)])
        while q:
            cur, pre = q.popleft()
            for k, v in cur.items():
                if k == _END:
                    words.append(pre)
                else:
                    q.append((v, pre + k))

        return words

    def _traverse(self, word: str) -> Union[None, dict]:
        ptr = self.root
        for c in word:
            if c in ptr:
                ptr = ptr[c]
            else:
                return None

        return ptr


def run():
    t = Trie("foo", "bar", "baz", "barz")

    assert not t.is_prefix("a")
    assert t.is_prefix("b")
    assert t.is_prefix("ba")
    assert t.is_prefix("barz")

    assert ["foo"] == t.words_with_prefix("f")
    assert ["bar", "barz"] == t.words_with_prefix("bar")
    assert ["bar", "barz", "baz"] == list(sorted(t.words_with_prefix("ba")))

    assert not t.contains("ba")
    assert t.contains("bar")
    assert t.contains("barz")

    assert not t.contains("fo")
    assert t.contains("foo")

    assert t.delete("foo")
    assert not t.contains("foo")

    assert t.delete("barz")
    assert not t.contains("barz")
    assert t.contains("bar")


run()
