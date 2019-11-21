class Solution:
    def get_range(self, a: list, target: int) -> list:
        left = self.binary_search_iter(a, 0, len(a) - 1, target, find_first=True)
        right = self.binary_search_iter(a, 0, len(a) - 1, target, find_first=False)
        return [left, right]

    def binary_search_iter(self, a: list, low: int, high: int, target: int, find_first: bool):
        while True:
            if low > high:
                return -1

            mid = (low + high) // 2
            if find_first:
                if a[mid] == target and (mid == 0 or a[mid - 1] != target):
                    # match and either at start or left spot doesn't match target
                    return mid

                if target > a[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if a[mid] == target and (mid == len(a) - 1 or a[mid + 1] != target):
                    return mid

                if target < a[mid]:
                    high = mid - 1
                else:
                    low = mid + 1


for array in [
    [1, 3, 3, 9, 9, 15],
    [9, 9, 10],
    [8, 9, 9],
    [9, 9, 9, 9, 9, 9]
]:
    print(
        Solution().get_range(
            a=array,
            target=9
        )
    )
