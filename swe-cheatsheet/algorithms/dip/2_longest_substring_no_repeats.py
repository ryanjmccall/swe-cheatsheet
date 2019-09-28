# Given a string, find the length of the longest substring without repeating characters.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        longest_substring_length = 0
        unique_chars = set()
        while right < len(s):
            char = s[right]
            if char in unique_chars:
                unique_chars.remove(s[left])
                left += 1
            else:
                # we can extend the longest substring by 1
                unique_chars.add(char)
                longest_substring_length = max(longest_substring_length, len(unique_chars))
                right += 1

        return longest_substring_length


print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10
