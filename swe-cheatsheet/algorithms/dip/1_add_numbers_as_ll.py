
"""
You are given two linked-lists representing two non-negative integers. The digits are stored in reverse order and
each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

Here is the function signature as a starting point (in Python):

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def add_two_numbers(self, list_1: ListNode, list_2: ListNode) -> ListNode:
        carry_over = 0
        head_sum = None
        prev_sum = None
        while list_1 or list_2:
            # invariants: 1) l1 or l2 has numbers, 2) carry represents previous carry value, 3) l1, l2 unsummed
            place_sum = carry_over
            if list_1:
                place_sum += list_1.val
                list_1 = list_1.next

            if list_2:
                place_sum += list_2.val
                list_2 = list_2.next

            if place_sum > 9:
                carry_over = 1
                place_sum %= 10
            else:
                carry_over = 0

            node = ListNode(place_sum)
            if head_sum is None:
                head_sum = node
            else:
                prev_sum.next = node

            prev_sum = node

        return head_sum


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().add_two_numbers(l1, l2)
while result:
    print(result.val)
    result = result.next
# 7 0 8
