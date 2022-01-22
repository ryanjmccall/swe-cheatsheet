from collections import defaultdict

class Solution(object):

    def get_anagram_indices(self, a: str, b: str) -> int:
        window = defaultdict(int)
        for c in b:
            window[c] += 1

        indices = list()
        for i, c in enumerate(a):
            if i >= len(b):
                c_old = a[i - len(b)]
                window[c_old] += 1
                if window[c_old] == 0:
                    del window[c_old]

            window[c] -= 1
            if window[c] == 0:
                del window[c]

            if i + 1 >= len(b) and len(window) == 0:
                indices.append(i - len(b) + 1)

        return indices


print(Solution().get_anagram_indices(a='acdbacdacb', b='abc'))
