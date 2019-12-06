from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        limit = 2 * n
        def dfs(cur: str, left: int, right: int):
            if len(cur) == limit:
                res.append(cur)
                return

            if left < n:
                dfs(cur + '(', left + 1, right)

            if left > right:
                dfs(cur + ')', left, right + 1)

        dfs(cur='', left=0, right=0)
        return res


for line in Solution().generateParenthesis(3):
    print(line)
