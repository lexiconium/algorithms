# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit, min_p = 0, float("inf")

        for p in prices:
            max_profit = max(p - min_p, max_profit)
            min_p = min(p, min_p)

        return max_profit
