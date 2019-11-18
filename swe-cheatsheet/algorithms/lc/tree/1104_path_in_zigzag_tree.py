"""
Zig Zag Binary Tree:
             1
           /   \
         3       2  <- 3+2-3 = 2/2 = 1
       /  \     /  \
     4     5   6     7   <- 7+4-4 = 7/2 = 3
   / |    /|   |\    | \
 15 14  13 12 11 10  9  8   <- 15+8-14 = 9/2 = 4
"""
from typing import List


class Solution:
    def pathInZigZagTree(self, value: int) -> List[int]:
        path = [value]

        greater_power_of_two = 2
        while value >= greater_power_of_two:
            greater_power_of_two *= 2

        while value != 1:
            # find complement
            upper_bound = greater_power_of_two - 1
            lower_bound = greater_power_of_two / 2
            complement = lower_bound + upper_bound - value
            value = int(complement / 2)
            path.append(value)
            greater_power_of_two /= 2

        path.reverse()
        return path


def test():
    s = Solution()
    for n in range(1, 16):
        path = s.pathInZigZagTree(n)
        print(path)


test()
