class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        char_to_ind = dict()
        left = 0
        for right, char in enumerate(s):
            if char in char_to_ind:
                left = max(left, char_to_ind[char] + 1)

            char_to_ind[char] = right
            longest = max(longest, right - left + 1)
        return longest


print(Solution().lengthOfLongestSubstring(s=""))  # 0
print(Solution().lengthOfLongestSubstring(s="abba"))  # 2
print(Solution().lengthOfLongestSubstring(s="dvdf"))  # 3
