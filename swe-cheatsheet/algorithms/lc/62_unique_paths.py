class Solution:
    def uniquePaths(self, w: int, h: int) -> int:
        row = [1] * w
        for _ in range(1, h):
            for j in range(1, w):
                row[j] += row[j-1]
        return row[-1]


print(Solution().uniquePaths(w=3, h=2))
print(Solution().uniquePaths(w=7, h=3))
