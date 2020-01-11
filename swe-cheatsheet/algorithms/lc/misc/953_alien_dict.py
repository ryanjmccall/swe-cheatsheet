from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        stone = {c: i for i, c in enumerate(order)}
        words = [[stone[c] for c in w] for w in words]
        return all(a <= b for a, b in zip(words, words[1:]))




print(Solution().isAlienSorted(
    ["hello", "leetcode"],
    "hlabcdefgijkmnopqrstuvwxyz"
)
)
