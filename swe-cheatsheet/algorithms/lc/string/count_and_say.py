class Solution:
    def countAndSay(self, n: int) -> str:
        # 1.     1
        # 2.     11
        # 3.     21
        # 4.     1211
        # 5.     111221
        if n == 1:
            return '1'

        say = [1]
        for _ in range(n - 1):
            next_say = []
            count = 0
            val = say[0]
            for v in say:
                if v == val:
                    count += 1
                else:
                    next_say.extend((count, val))
                    count = 1
                    val = v

            next_say.extend((count, val))
            say = next_say

        return ''.join((str(v) for v in say))



s = Solution()
for num_ in range(1, 6):
    print(f'{num_}: {s.countAndSay(num_)}')
