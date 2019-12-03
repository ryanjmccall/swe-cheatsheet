from typing import List


class Solution:
    def totalFruit(self, trees: List[int]) -> int:
        if not trees:
            return 0

        max_total = 1
        total = 1
        tree_to_ind = {trees[0]: 0}
        for i in range(1, len(trees)):
            if trees[i] in tree_to_ind or len(tree_to_ind) < 2:
                total += 1
            else:
                # end current subarray
                max_total = max(max_total, total)

                # find start of next subarray
                prev = trees[i - 1]
                other = [k for k in tree_to_ind if k != prev][0]
                total = i - tree_to_ind[other]
                del tree_to_ind[other]

            tree_to_ind[trees[i]] = i

        return max(max_total, total)


assert Solution().totalFruit(trees=[3,3,3,1,2,1,1,2,3,3,4]) == 5
