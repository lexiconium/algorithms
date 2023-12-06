# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/solutions/3667440/beats-100-c-java-python-beginner-friendly


class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        profit_holding_a_stock, profit = float("-inf"), 0

        for p in prices:
            profit_holding_a_stock = max(profit - p, profit_holding_a_stock)
            profit = max(profit_holding_a_stock + p - fee, profit)

        return profit
