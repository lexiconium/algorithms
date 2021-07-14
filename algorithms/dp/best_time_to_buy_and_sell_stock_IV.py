# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

# time complexity: O(kn)

class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        bought, sold = [float('-inf')] * (k + 1), [0] * (k + 1)
        for p in prices:
            for i in range(1, k + 1):
                sold[i] = max(sold[i], bought[i] + p)
                bought[i] = max(bought[i], sold[i - 1] - p)
        return sold[-1]