"""
Given a sorted array, A, with possibly duplicated elements, find the indices of the first and last occurrences of a
target element, x. Return -1 if the target is not found.

Example:

Input: A = [1, 3, 3, 5, 7, 8, 9, 9, 9, 15], target = 9
Output: [6, 8]

Input: A = [100, 150, 150, 153], target = 150
Output: [1, 2]

Input: A = [1, 2, 3, 4, 5, 6, 10], target = 9
Output: [-1, -1]
"""
from typing import List


class Solution:
    @classmethod
    def get_range(cls, array, target) -> (int, int):
        left_bound = cls._get_single_range_bound(array, target, is_left=True)
        right_bound = cls._get_single_range_bound(array, target, is_left=False)
        return [left_bound, right_bound]

    @classmethod
    def _get_single_range_bound(cls, array, target, is_left: bool) -> int:
        """Given a sorted array possibly with duplicates, returns one of the boundary index of the target value

        (1, 2, [2], 2, 1), or (1, [2], 2), or (2, [2], 3)

        :param array: an array of sorted values
        :param target: value whose bounds are sought
        :param is_left: if True, returns the left boundary of range, else return right boundary
        :return:
        """
        left = 0
        right = len(array) - 1
        while left <= right:
            mid = (left + right) // 2
            if array[mid] < target:
                left = mid + 1
            elif array[mid] > target:
                right = mid - 1
            else:
                # found target
                if is_left:
                    # check just left of mid
                    if mid == 0:
                        return mid

                    if array[mid - 1] != target:
                        return mid

                    # search left
                    right = mid - 1
                else:
                    # check just right of mid
                    if mid == len(array) - 1:
                        return mid

                    if array[mid + 1] != target:
                        return mid

                    # search right
                    left = mid + 1

        return -1


def main():
    a = [0, 1, 2, 2, 3, 4, 5, 6, 7, 8]
    x = 2
    print(Solution().get_range(a, x))


main()
