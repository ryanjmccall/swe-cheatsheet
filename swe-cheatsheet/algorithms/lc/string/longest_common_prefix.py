from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        min_size = min(len(w) for w in strs)
        i = 0
        for i in range(min_size):
            if not all(strs[0][i] == w[i] for w in strs[1:]):
                break

        return strs[0][:i + 1]


    def lcp(self, m):
        if not m: return ''
        s1 = min(m)
        s2 = max(m)
        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i]

        return s1


print(Solution().longestCommonPrefix(['a']))
print(Solution().lcp(['aa', 'a']))

