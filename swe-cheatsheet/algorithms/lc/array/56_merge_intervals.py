from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        for start, end in sorted(intervals, key=lambda i: i[0]):
            if res and start <= res[-1][1]:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start, end])
        return res


print(Solution().merge(intervals=[[1,3],[2,6],[8,10],[15,18]]))
