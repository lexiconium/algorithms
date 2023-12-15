# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0

        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                profit += prices[i + 1] - prices[i]

        return profit

    def maxProfit(self, prices: list[int]) -> int:
        profit_holding_prev, profit = float("-inf"), 0

        for p in prices:
            profit_holding_prev = max(profit - p, profit_holding_prev)
            profit = max(profit_holding_prev + p, profit)

        return profit
