_ROMAN_TO_DECIMAL = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


class Solution:
    def romanToInt(self, s: str) -> int:
        if not s: return 0
        prev = _ROMAN_TO_DECIMAL[s[0]]
        total = prev
        for c in s[1:]:
            val = _ROMAN_TO_DECIMAL[c]
            if prev > val:
                total += val
            else:
                total += val - 2*prev
            prev = val

        return total


print(Solution().romanToInt("MCMXCIV"))