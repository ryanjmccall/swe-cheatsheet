class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 1: return 0
        if n == 2: return 1
        nums = {i for i in range(2, n + 1)}
        for i in range(2, n):
            for j in range(i + i, n + 1, i):
                if j in nums:
                    nums.remove(j)
        return len(nums)


def t():
    # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    print(Solution().countPrimes(n=10))


t()
