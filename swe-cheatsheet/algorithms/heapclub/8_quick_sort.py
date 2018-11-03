#!/usr/bin/env python

def partition(a, begin, end):
    pivot = begin
    for i in range(begin + 1, end + 1):
        if a[i] <= a[pivot]:
            a[i], a[pivot] = a[pivot], a[i]
            pivot += 1

    a[pivot], a[end] = a[end], a[pivot]
    return pivot


def qsort(array, left=0, right=None):
    if right is None:
        right = len(array) - 1

    def _qsort(l, r):
        if l < r:
            pivot = partition(array, l, r)
            _qsort(l, pivot - 1)
            _qsort(pivot + 1, r)

    return _qsort(left, right)


_array = [3, 2, 6, 7, 1]
qsort(_array)
print(_array)
