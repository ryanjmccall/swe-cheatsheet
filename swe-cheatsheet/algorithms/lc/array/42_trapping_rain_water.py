class Solution:
    def trap(self, height):
        l = 0
        r = len(height) - 1
        level = 0
        water = 0
        while l < r:
            if height[l] < height[r]:
                ind = l
                l += 1
            else:
                ind = r
                r -= 1
            lower = height[ind]
            if lower > level:
                level = lower
            print(f'{ind} {level-lower}')
            water += level - lower
        return water


print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6)
