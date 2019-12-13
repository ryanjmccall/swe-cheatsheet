from typing import List
class S(object):
    def compress(self, arr: List[int]) -> List[List[int]]:
        if not arr: return []
        res = []
        left = 0
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] not in (0, 1):
                res.append([arr[left], arr[i - 1]])
                left = i

        res.append([arr[left], arr[len(arr) - 1]])
        return res


def t():
    print(S().compress(arr=[0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]))


t()
