class Solution:
    def findNthDigit(self, nth):
        """
        :type nth: int
        :rtype: int
        """
        start = 1
        digiSize = 1
        step = 9
        while nth > digiSize * step:
            nth -= digiSize * step
            start *= 10
            digiSize += 1
            step *= 10

        digitStart = start + (nth - 1) // digiSize
        digitIdx = (nth - 1) % digiSize
        return int(str(digitStart)[digitIdx])


print(Solution().findNthDigit(11))
