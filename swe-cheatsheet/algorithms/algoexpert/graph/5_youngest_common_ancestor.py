# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    visited = set()
    a, b = descendantOne, descendantTwo
    while a or b:
        if a:
            if a.name in visited:
                return a
            visited.add(a.name)
            a = a.ancestor

        if b:
            if b and b.name in visited:
                return b
            visited.add(b.name)
            b = b.ancestor

    return None
