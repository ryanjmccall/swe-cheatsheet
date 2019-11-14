from typing import List


class Node:
    def __init__(self, id_: int, amount: float):
        self.id = id_
        self.amount = amount


class Allocation:
    def __init__(self, source: Node, sink: Node, amount: float):
        self.source = source
        self.sink = sink
        self.amount = amount

    def __str__(self):
        return '%s, %s, %s' % (self.source.id, self.sink.id, self.amount)


"""
Devise an algorithm that allocates (assigns) amounts from the first group of Nodes to the second group of Nodes. 
"""


class Solution(object):

    def __init__(self):
        self.allocations = []

    def allocate(self, sources: List[Node], sinks: List[Node]):
        a = [n for n in sources if n.amount]
        b = [n for n in sinks if n.amount]
        a_ptr = 0
        b_ptr = 0
        while a_ptr < len(a) and b_ptr < len(b):
            amount = min(a[a_ptr].amount, b[b_ptr].amount)
            self.allocations.append(Allocation(source=a[a_ptr], sink=b[b_ptr], amount=amount))
            a[a_ptr].amount -= amount
            if not a[a_ptr].amount:
                a_ptr += 1

            b[b_ptr].amount -= amount
            if not b[b_ptr].amount:
                b_ptr += 1   # 14 loc


def main():
    a = [Node(0, 10), Node(1, 5)]
    b = [Node(2, 5), Node(3, 6), Node(4, 100)]
    s = Solution()
    s.allocate(a, b)
    for alloc in s.allocations:
        print(alloc)


main()
