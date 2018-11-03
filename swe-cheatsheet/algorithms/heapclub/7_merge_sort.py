#!/usr/bin/env python


def merge(left: list, right: list):
    l = r = 0
    merged = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            merged.append(left[l])
            l += 1
        else:
            merged.append(right[r])
            r += 1

    return (merged + right[r:]
            if l == len(left)
            else merged + left[l:])


def mergeSort(array: list):
    if len(array) < 2:
        return array

    mid = len(array) // 2
    left = mergeSort(array[:mid])
    right = mergeSort(array[mid:])
    return merge(left, right)


if __name__ == "__main__":
    a = [38, 27, 43, 3, 9, 83, 10]
    print(mergeSort(a))

