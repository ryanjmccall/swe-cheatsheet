class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = [c.lower() for c in s if c.isalnum() and c != ' ']
        size = len(chars)
        for i in range(size // 2):
            if chars[i] != chars[size - 1 - i]:
                return False
        return True


print(Solution().isPalindrome('a man a plan a canal: panama'))
print(Solution().isPalindrome('abcdefg'))
