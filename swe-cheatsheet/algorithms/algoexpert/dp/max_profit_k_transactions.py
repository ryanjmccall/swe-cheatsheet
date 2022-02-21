
def maxProfitWithKTransactions(prices: list, k: int) -> int:
    """
    time: O(nk)
    space: O(nk)
    """
    if not prices:
        return 0

    profits = [[0] * len(prices) for _ in range(k + 1)]
    for t in range(1, k + 1):
        cur_max = float('-inf')
        for d in range(1, len(prices)):
            cur_max = max(cur_max, profits[t -1][d -1] - prices[d -1])
            profits[t][d] = max(profits[t][d -1], cur_max + prices[d])

    return profits[-1][-1]


def maxProfitWithKTransactions2(prices: list, k: int) -> int:
    """
    time: O(nk)
    space: O(n)
    """
    if not prices:
        return 0
    even_profits = [0] * len(prices)
    odd_profits = [0] * len(prices)
    for t in range(1, k + 1):
        cur_profits, prev_profits = (odd_profits, even_profits) if t % 2 else (even_profits, odd_profits)
        cur_max = float('-inf')
        for d in range(1, len(prices)):
            cur_max = max(cur_max, prev_profits[d-1] - prices[d-1])
            cur_profits[d] = max(cur_profits[d-1], cur_max + prices[d])

    return odd_profits[-1] if k % 2 else even_profits[-1]


print(maxProfitWithKTransactions([5, 11, 3, 50, 60, 90], k=2))  # 93
print(maxProfitWithKTransactions2([5, 11, 3, 50, 60, 90], k=2))  # 93


