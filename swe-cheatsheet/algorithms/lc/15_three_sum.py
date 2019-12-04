


class Solution(object):


    def three_sum_(self, arr):
        res = []
        length = len(arr)
        for i, n in enumerate(arr[:-2]):
            if n > 0:
                break

            if i and arr[i-1] == arr[i]:
                continue

            left = i + 1
            right = length - 1
            while left < right:
                total = n + arr[left] + arr[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([n, arr[left], arr[right]])


                    while left < right and arr[left] == arr[left + 1]:
                        left += 1
                    while left < right and arr[right - 1] == arr[right]:
                        right -= 1

                    left += 1
                    right -= 1

        return res

    def threeSum(self, nums):
        if len(nums) < 3:
            return []

        negatives = []
        zeros = 0
        positives = []
        for n in nums:
            if n < 0:
                negatives.append(n)
            elif n > 0:
                positives.append(n)
            else:
                zeros += 1

        res = set()
        if zeros >= 3:  # Case: (0, 0, 0)
            res.add((0, 0, 0))

        # Case: (0, x, -x)
        pos_set = set(positives)
        neg_set = set(negatives)
        if zeros > 0:
            if len(positives) < len(negatives):
                other_set = neg_set  # fewer array iterations
                vals = positives
            else:
                other_set = pos_set
                vals = negatives

            for v in vals:
                if -v in other_set:
                    if v > 0:
                        res.add((-v, 0, v))
                    else:
                        res.add((v, 0, -v))

        # Case 2-pos, 1-neg and 1-neg, 2-pos
        self._one_two_case(res, negatives, pos_set)
        self._one_two_case(res, positives, neg_set)
        return list(res)

    def _one_two_case(self, res, twos: list, ones: set):
        for i, a in enumerate(twos[:-1]):
            for b in twos[i + 1:]:
                if -(a + b) in ones:
                    if a > b:
                        res.add((b, a, -(a + b)))
                    else:
                        res.add((a, b, -(a + b)))



