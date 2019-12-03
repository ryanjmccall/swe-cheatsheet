
LIMIT = pow(2, 31)
class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            positive = True
        else:
            positive = False
            x = x * -1

        digits = []
        while x:
            digits.append(str(x % 10))
            x //= 10

        val = int(''.join(digits))

        if val >= LIMIT or val <= -LIMIT:
            return 0

        return val if positive else -val


