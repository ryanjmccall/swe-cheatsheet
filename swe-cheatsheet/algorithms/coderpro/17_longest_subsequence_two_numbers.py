
class Solution(object):
    def findSequence_(self, seq: list) -> int:
        if len(seq) < 2:
            return len(seq)

        length = 0
        max_length = 0
        a, b = seq[0], seq[1]
        last_num = b
        last_num_count = 1 if a == b else 0
        for n in seq[1:]:
            if n in (a, b):
                # current sequence increases
                length += 1

                # update last num vars
                if n == b:
                    last_num_count += 1
                else:
                    last_num = a
                    last_num_count = 1

            else:
                a = last_num
                b = n
                last_num = b
                length = last_num_count + 1
                last_num_count = 1

            max_length = max(max_length, length)

        return max_length

    def findSequence(self, seq):
        if len(seq) < 2:
            return len(seq)

        a, b = seq[0], seq[1]

        last_num = b
        last_num_count = 2 if (a == b) else 1
        length = 2
        max_length = 2
        for n in seq[2:]:
            if n in (a, b):
                length += 1
                if b == n:
                    last_num_count += 1
                else:
                    last_num = a
                    last_num_count = 1
            else:
                length = last_num_count + 1
                a = last_num
                b = n
                last_num = n
                last_num_count = 1

            max_length = max(length, max_length)

        return max_length


print(Solution().findSequence(seq=[3, 1, 1, 3, 5, 3, 1, 3, 1, 5]))
print(Solution().findSequence(seq=[3, 1, 1]))
