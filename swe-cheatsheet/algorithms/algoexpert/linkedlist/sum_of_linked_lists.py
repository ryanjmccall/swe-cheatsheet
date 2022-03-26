# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f'{self.value}'


def sumOfLinkedLists1(list1, list2):
    if not list1:
        return list2

    if not list2:
        return list1

    head = LinkedList((list1.value + list2.value) % 10)
    carryover = (list1.value + list2.value) // 10
    list1 = list1.next
    list2 = list2.next
    prev = head
    while list1 or list2 or carryover:
        val_sum = (list1.value if list1 else 0) + (list2.value if list2 else 0) + carryover
        prev.next = LinkedList(val_sum % 10)
        carryover = val_sum // 10

        prev = prev.next
        list1 = list1.next if list1 else None
        list2 = list2.next if list2 else None

    return head


def sumOfLinkedLists(l1, l2):
    """Let n = num nodes l1 + num nodes l2
    Time: O(n)
    Space: O(1)
    """
    dummy_node = LinkedList(None)
    cur_node = dummy_node
    carryover = 0
    n1, n2 = l1, l2
    while n1 or n2 or carryover:
        v1 = n1.value if n1 else 0
        v2 = n2.value if n2 else 0
        value_sum = v1 + v2 + carryover
        carryover = value_sum // 10
        ones_digit = value_sum % 10
        cur_node.next = LinkedList(ones_digit)

        # advance pointers
        cur_node = cur_node.next
        n1 = n1.next if n1 else None
        n2 = n2.next if n2 else None

    return dummy_node.next


a = LinkedList(2, LinkedList(4, LinkedList(7, LinkedList(1))))
b = LinkedList(9, LinkedList(4, LinkedList(5)))
r = sumOfLinkedLists(a, b)
while r:
    print(r.value)
    r = r.next