from typing import List


class Node:
    def __init__(self, children: dict):
        self.terminal = False
        self.children = children


class Autocomplete(object):
    def __init__(self, words):
        trie = Node(children={})
        for w in words:
            ptr = trie
            for c in w:
                if c not in ptr.children:
                    ptr.children[c] = Node(children={})
                ptr = ptr.children[c]
            ptr.terminal = True
        self.trie = trie

    def get_words(self, prefix: str) -> List[str]:
        n = self.trie
        for c in prefix:
            if c not in n.children:
                return []
            n = n.children[c]

        words = []
        stk = [(prefix, n)]
        while stk:
            pre, ptr = stk.pop()
            if ptr.terminal:
                words.append(pre)
            stk.extend((pre + c, child) for c, child in ptr.children.items())
        return words


def test():
    ac = Autocomplete(words=['dog', 'dogs'])
    print(ac.get_words(prefix='do'))
    print(ac.get_words(prefix='dog'))
    print(ac.get_words(prefix='dogs'))
    print(ac.get_words(prefix='dogsz'))


test()
