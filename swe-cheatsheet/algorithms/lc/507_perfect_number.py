from math import sqrt, ceil


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False

        _sum = 1
        for i in range(2, ceil(sqrt(num))):
            if num % i == 0:
                _sum += i + num / i

        return _sum == num


print(Solution().checkPerfectNumber(28))
