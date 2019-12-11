from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        count = 0
        height = len(grid)
        width = len(grid[0])
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == '1':
                    stack = [(i, j)]
                    while stack:
                        ci, cj = stack.pop()
                        grid[ci][cj] = '-1'
                        if ci and grid[ci - 1][cj] == '1':
                            stack.append((ci - 1, cj))

                        if ci < height - 1 and grid[ci + 1][cj] == '1':
                            stack.append((ci + 1, cj))

                        if cj and grid[ci][cj - 1] == '1':
                            stack.append((ci, cj - 1))

                        if cj < width - 1 and grid[ci][cj + 1] == '1':
                            stack.append((ci, cj + 1))

                    count += 1

        return count


__grid = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1']
]
print(Solution().numIslands(__grid))
