from typing import List


class Solution:
    def generate(self, rows: int) -> List[List[int]]:
        tri = [[1]]
        prev = tri[0]
        for r in range(rows):
            row = [1]
            for i in range(1, r+1):
                row.append(prev[i - 1] + prev[i])

            row.append(1)
            tri.append(row)
            prev = row

        return tri


for x in Solution().generate(rows=5):
    print(x)
