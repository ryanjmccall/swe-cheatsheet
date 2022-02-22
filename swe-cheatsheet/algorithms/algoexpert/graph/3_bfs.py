# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        q = [self]
        visited = set()
        for cur in q:
            array.append(cur.name)
            visited.add(cur.name)
            q.extend(v for v in cur.children if v not in visited)
        return array
