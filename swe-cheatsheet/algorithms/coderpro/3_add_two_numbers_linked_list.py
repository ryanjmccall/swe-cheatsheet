class Node(object):
    def __init__(self, v):
        self.val = v
        self.next = None


class Solution:
    def add_two_numbers(self, l1: Node, l2: Node):
        carry = 0
        head = current = None
        while l1 or l2:
            val = l1.val + l2.val + carry
            carry = val // 10
            if current:
                current.next = Node(val % 10)
                current = current.next
            else:
                head = current = Node(val % 10)

            if l1.next or l2.next:
                # fill in 0s if missing, else advance and end while
                if not l1.next:
                    l1.next = Node(0)
                if not l2.next:
                    l2.next = Node(0)

            l1 = l1.next
            l2 = l2.next

        return head

    def add_two_numbers_recur(self, l1, l2):
        return self.helper(l1, l2, 0)

    def helper(self, l1, l2, carry):
        val = l1.val + l2.val + carry
        carry = val // 10
        ret = Node(val % 10)
        if l1.next or l2.next:
            if not l1.next:
                l1.next = Node(0)
            if not l2.next:
                l2.next = Node(0)
            ret.next = self.helper(l1.next, l2.next, carry)

        return ret


def main():
    l1 = Node(2)
    l1.next = Node(4)
    l1.next.next = Node(3)

    l2 = Node(5)
    l2.next = Node(6)
    l2.next.next = Node(4)

    # 342
    # 465
    # 807
    answer = Solution().add_two_numbers(l1, l2)
    # answer = Solution().add_two_numbers_recur(l1, l2)
    while answer:
        print(answer.val)
        answer = answer.next


main()
