# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75928/Share-my-DP-solution-(By-State-Machine-Thinking)

# time complexity: O(n)

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        sold, hold, rest = 0, float('-inf'), 0
        for p in prices:
            prev_sold = sold
            
            sold = hold + p
            hold = max(hold, rest - p)
            rest = max(rest, prev_sold)
        return max(sold, rest)