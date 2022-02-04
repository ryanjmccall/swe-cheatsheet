class OptListSum(object):
    def __init__(self, a: list):
        self.memo = [0]
        total = 0
        for v in a:
            total += v
            self.memo.append(total)

    def get_sum(self, i: int, j: int) -> int:
        if i < 0 or i >= j or j > len(self.memo):
            raise ValueError(f'Range {i} {j} not within [0, {len(self.memo)})')

        return self.memo[j] - self.memo[i]


ols = OptListSum([1, 2, 3, 4, 5, 6, 7])
print(ols.get_sum(2, 5))
