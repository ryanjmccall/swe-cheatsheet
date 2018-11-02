#!/usr/bin/env python


class Stack:
    def __init__(self):
        self.a = []

    def push(self, v):
        self.a.append(v)

    def pop(self):
        return self.a.pop() if self.a else None

    def size(self):
        return len(self.a)

    def is_empty(self) -> bool:
        return True if self.a else False


class Node:
    def __init__(self, v):
        self.next = None
        self.prev = None
        self.val = v


class Queue:
    def __init__(self):
        self.head = None  # first to remove
        self.tail = None  # last to remove
        # head < x < y < ... < tail

    def enqueue(self, v):
        n = Node(v)
        if self.head:
            n.next = self.tail
            self.tail.prev = n
        else:
            self.head = n

        self.tail = n

    def dequeue(self):
        result = self.head
        self.head = result.prev

        # delete both pointers
        result.prev = None
        self.head.next = None
        return result
