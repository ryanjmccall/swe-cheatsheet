#!/usr/bin/env python

def combinations(arr, carry):
    for i in range(len(arr)):
        yield carry + arr[i]
        yield from combinations(arr[i + 1:], carry + arr[i])

# where initially carry = "".
