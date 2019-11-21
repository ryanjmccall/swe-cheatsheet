class Solution(object):

    def single_number(self, nums):
        seen = set()
        for n in nums:
            if n in seen:
                seen.remove(n)
            else:
                seen.add(n)
        return seen.pop()

    def single_number_2(self, nums):
        result = 0
        for n in nums:
            result ^= n
            print(result)
        return result


print(Solution().single_number(nums=[4, 3, 2, 4, 1, 3, 2]))
print(Solution().single_number_2(nums=[4, 3, 2, 4, 1, 3, 2]))

