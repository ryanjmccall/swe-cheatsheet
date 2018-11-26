class Solution:
    def countBinarySubstrings2(self, s) -> int:
        """
        :type s: str
        :rtype: int
        """
        substrings = 0
        zeros = 0
        ones = 0

        prev = s[0]
        if prev == "0":
            zeros += 1
        else:
            ones += 1

        # 0, 0
        # 1, 0
        # 1, 1
        frontCompleted = False
        for c in s[1:]:
            if prev != c:
                if frontCompleted:
                    frontCompleted = False
                    if zeros == ones:
                        substrings += 1

                    zeros = 0
                    ones = 0
                else:
                    frontCompleted = True

            prev = c

            if c == "0":
                zeros += 1
            else:
                ones += 1

        return substrings

    def countBinarySubstrings(self, s) -> int:
        prevRunLength = 0
        curRunLength = 1
        res = 0
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                curRunLength += 1
            else:
                prevRunLength = curRunLength
                curRunLength = 1

            if prevRunLength >= curRunLength:
                res += 1

        return res


print(Solution().countBinarySubstrings("00110"))
