# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# time complexity: O(n)

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        min_price = float('inf')
        for p in prices:
            min_price = min(min_price, p)
            profit = max(profit, p - min_price)
        return profit