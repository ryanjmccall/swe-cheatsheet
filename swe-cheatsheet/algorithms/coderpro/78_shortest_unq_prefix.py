
class Node:
    def __init__(self):
        self.count = 0
        self.children = dict()


class Trie(object):
    def __init__(self):
        self.root = Node()

    def insert(self, w: str):
        ptr = self.root
        for c in w:
            if c not in ptr.children:
                ptr.children[c] = Node()
            ptr.count += 1
            ptr = ptr.children[c]

    def shortest_prefix(self, w: str):
        ptr = self.root
        pre = ''
        for c in w:
            if ptr.count == 1:
                break

            ptr = ptr.children[c]
            pre += c

        return pre


def shortest_unique_prefix(words):
    t = Trie()
    for w in words:
        t.insert(w)

    return [t.shortest_prefix(w) for w in words]


print(shortest_unique_prefix(words=['abc', 'abd', 'doc', 'drop']))
print(shortest_unique_prefix(words=['jon', 'john', 'jack', 'techlead']))
