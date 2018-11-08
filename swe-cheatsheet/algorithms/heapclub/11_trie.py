
_END = "_end_"


class Trie:
    def __init__(self):
        self.root = dict()

    def makeTrie(self, *words):
        self.root = dict()
        for w in words:
            self._insert(self.root, w)

    @staticmethod
    def _insert(node: dict, word: str):
        for l in word:
            if l not in node:
                node[l] = dict()

            node = node[l]

        node[_END] = None

    def contains(self, word: str) -> bool:
        cur = self.root
        for l in word:
            if l in cur:
                cur = cur[l]
            else:
                return False

        # case where "roommate" in trie but not "room"
        return _END in cur

    def insert(self, word: str):
        self._insert(self.root, word)

    def remove(self, word: str) -> bool:
        cur = self.root
        path = []
        for l in word:
            if l in cur:
                path.append(cur)
                cur = cur[l]
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


def run():
    t = Trie()
    t.makeTrie("foo", "bar", "baz", "barz")

    assert not t.contains("ba")
    assert t.contains("bar")
    assert t.contains("barz")

    assert not t.contains("fo")
    assert t.contains("foo")

    assert t.remove("foo")
    assert not t.contains("foo")

    assert t.remove("barz")
    assert not t.contains("barz")
    assert t.contains("bar")


run()
