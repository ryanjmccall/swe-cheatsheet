class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = '' if numerator * denominator > 0 else '-'
        numerator = abs(numerator)
        denominator = abs(denominator)
        n, numerator = divmod(numerator, denominator)
        res = [sign + str(n)]
        if numerator:
            res.append('.')
        i = len(res)
        numer_to_index = dict()
        while numerator:
            if numerator in numer_to_index:
                i = numer_to_index[numerator]
                return ''.join(res[:i])  + '(' + ''.join(res[i:]) + ')'
            else:
                numer_to_index[numerator] = i

            n, numerator = divmod(numerator * 10, denominator)
            res.append(str(n))
            i += 1

        return ''.join(res)



print(Solution().fractionToDecimal(5, 2))
print(Solution().fractionToDecimal(2, 1))
print(Solution().fractionToDecimal(1, 2))
print(Solution().fractionToDecimal(-2, -3))
print(Solution().fractionToDecimal(2, -3))
print(Solution().fractionToDecimal(1, 6))
