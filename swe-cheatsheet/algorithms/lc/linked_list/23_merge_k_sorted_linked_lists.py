from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from heapq import heappop, heappush, heapify
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        Must add additional value 'i' because:
        Tuple comparison breaks for (priority, task) pairs if the priorities are equal
        and the tasks do not have a default comparison order.

        A solution to the first two challenges is to store entries as 3-element list
        including the priority, an entry count, and the task. The entry count serves as
        a tie-breaker so that two tasks with the same priority are returned in the order
        they were added. And since no two entry counts are the same, the tuple comparison
        will never attempt to directly compare two tasks.
        """
        cur = dummy = ListNode(None)
        heap = [(n.val, i, n) for i, n in enumerate(lists) if n]
        heapify(heap)
        while heap:
            val, i, n = heappop(heap)
            if n.next:
                heappush(heap, (n.next.val, i, n.next))
            cur.next = cur = n
        return dummy.next

    def mergeKLists_Onk(self, lists: List[ListNode]) -> ListNode:
        dummy = ListNode(None)
        prev = dummy
        while True:
            i_min = None
            val_min = float('inf')
            for i, head in enumerate(lists):
                if head and head.val < val_min:
                    val_min = head.val
                    i_min = i

            if i_min is None:
                break

            prev.next = lists[i_min]
            prev = lists[i_min]
            lists[i_min] = lists[i_min].next

        return dummy.next
