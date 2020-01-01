class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        index = dict()
        cur_len = 0
        for i, c in enumerate(s):
            if c in index:
                cur_len = i - index[c]
                # remove all entries before index[c]
            else:
                cur_len += 1
                index[c] = i

            if cur_len > longest:
                longest = cur_len

        return longest


print(Solution().lengthOfLongestSubstring(s="abba"))
