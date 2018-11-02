#!/usr/bin/env python

"""Implement a vector (mutable array with automatic resizing):
Practice coding using arrays and pointers, and pointer math to jump to an index
instead of using indexing.

Time
    O(1) to add/remove at end (amortized for allocations for more space),
    index, or update
    O(n) to insert/remove elsewhere

Space
    contiguous in memory, so proximity helps performance
    space needed = (array capacity, which is >= n) * size of item, but even if
    2n, still O(n)
"""

from math import ceil, log, pow
from typing import Any, Union


DEFAULT_SIZE = 16


def nextPowerOfTwo(n: int) -> int:
    return int(pow(2, ceil(log(n, 2))))


class ArrayList:
    def __init__(self, size=DEFAULT_SIZE):
        self.a = [None] * nextPowerOfTwo(size)
        self.ptr = 0  # where next element will be added, also the size

    def size(self) -> int:
        return self.ptr

    def capacity(self) -> int:
        return len(self.a)

    def is_empty(self) -> bool:
        return not self.ptr

    def at(self, index: int) -> Any:
        return self.a[index]

    def find(self, val: Any) -> int:
        for i, v in enumerate(self.a):
            if v == val:
                return i

        return -1

    def pop(self) -> Union[Any, None]:
        if not self.ptr: return None
        val = self.a[self.ptr]
        self.ptr -= 1
        self._remove_capacity()
        return val

    def delete(self, index: int):
        if index < 0 or index > self.ptr:
            raise ValueError("Index out of bounds")

        self.a = self.a[:index] + self.a[index + 1:] + [None]
        self.ptr -= 1
        self._remove_capacity()

    def remove(self, item: Any):
        """" O(n) time and O(n) space
        1, 1, 2, 2, 1, None, None, None  (8 items, 0-7)
        ptr = 5
        passed = 1, 1, 1  (len 3)
        """
        passed = filter(lambda x: x != item, self.a[:self.ptr])
        self.a = passed + [None] * (self.ptr - len(passed)) + self.a[self.ptr:]

    def push(self, v: Any):
        self._add_capacity()

        self.a[self.ptr] = v
        self.ptr += 1

    def insert(self, index: int, v: Any):
        if index < 0:
            raise ValueError("Index out of bounds")

        if index >= self.ptr:
            self.push(v)

        self._add_capacity()
        self.a = self.a[:index] + [v] + self.a[index:]

    def prepend(self, v: Any):
        self.insert(0, v)

    def _add_capacity(self):
        # allocate more space
        if self.ptr == len(self.a):
            self.a += [None] * (self.capacity() * 2 - len(self.a))

    def _remove_capacity(self):
        if self.ptr <= len(self.a) / 4:
            self.a = self.a[:len(self.a) / 2]
