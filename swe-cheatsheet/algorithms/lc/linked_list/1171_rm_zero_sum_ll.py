# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        cur = head
        sum_to_node = {}
        psum = 0
        while cur:
            psum += cur.val
            if psum == 0:
                head = cur.next
                sum_to_node.clear()
            else:
                if psum in sum_to_node:
                    prev = sum_to_node[psum]

                    # must delete dict entries for nodes from sum_to_node[psum] to current
                    # since these nodes will be removed from the list
                    del_sum = psum + prev.next.val
                    while del_sum != psum:
                        node = sum_to_node.pop(del_sum)
                        del_sum += node.next.val

                    prev.next = cur.next
                else:
                    sum_to_node[psum] = cur

            cur = cur.next

        return head
    