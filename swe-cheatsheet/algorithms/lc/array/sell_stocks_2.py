from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        min_index = 0
        prev = 0
        for current in range(1, len(prices)):
            if prices[prev] > prices[current]:
                # decrease

                # calculate current profit for selling at prev's value
                total_profit += prices[prev] - prices[min_index]

                # update min
                min_index = current

            prev = current

        # could have ended on a high so sell then
        total_profit += prices[prev] - prices[min_index]
        return total_profit


print(f'max profit: {Solution().maxProfit([7, 1, 5, 3, 6, 4])}')
