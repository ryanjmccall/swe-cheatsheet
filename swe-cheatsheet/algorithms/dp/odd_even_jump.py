
class Solution(object):


    def oddEvenJumps(self, a) -> int:
        # 1, 3, 5 odd jumps: jump to j such that a[i] <= a[j] and a[j] is smallest
        # 2, 4, 6 even jumps: jump to j such that a[i] >= a[j] and a[j] is largest
        n = len(a)
        b = sorted(range(n), key=lambda i: a[i])
        odd_next = self.make(b, n)

        b.sort(key=lambda i: -a[i])
        even_next = self.make(b, n)

        print(a)
        print(odd_next)
        print(even_next)

        odd = [False] * n
        even = [False] * n
        odd[n-1] = even[n-1] = True

        for i in reversed(range(n - 1)):
            if odd_next[i] is not None:
                odd[i] = even[odd_next[i]]
            if even_next[i] is not None:
                even[i] = odd[even_next[i]]


        return sum(odd)

    def make(self, b, n):
        ans = [None] * n
        stack = []  # stack is decreasing
        for i in b:
            while stack and i > stack[-1]:
                ans[stack.pop()] = i
            stack.append(i)

        return ans


def t():
    a = [10,13,12,14,15]
    print(Solution().oddEvenJumps(a))


t()
