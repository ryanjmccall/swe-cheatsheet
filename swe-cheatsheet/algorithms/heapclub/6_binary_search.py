#!/usr/bin/env python
from typing import Any


def binSearchItr(a: list, v: Any) -> int:
    s = 0
    e = len(a) - 1
    while e >= s:
        mid = int((s + e) / 2)
        if a[mid] < v:
            s = mid + 1
        elif a[mid] > v:
            e = mid - 1
        else:
            return mid

    return -1


def binSearchRecur(a: list, v: Any) -> int:
    def binSearch(s, e):
        mid = int((s + e) / 2)
        if a[mid] < v:
            return binSearch(mid + 1, e)
        elif a[mid] > v:
            return binSearch(s, mid - 1)

        return mid

    return binSearch(0, len(a) - 1)


def testSearch(a):
    print(a)
    print("val\titr\trecur")
    for v in sorted(set(a)):
        itrIdx = binSearchItr(a, v)
        recurIdx = binSearchRecur(a, v)
        print("%s\t%s\t%s" % (v, itrIdx, recurIdx))
    print()


def main():
    a = [0, 3, 5, 5, 5, 9, 10]
    testSearch(a)
    # expect 0, 1, 3, 5, 6

    a = [-10, -1, -1, 0, 1, 1, 2, 900, 999]
    testSearch(a)
    # expect 0, 1, 3, 4, 6, 7, 8


if __name__ == "__main__":
    main()
