# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/39611/Is-it-Best-Solution-with-O(n)-O(1).

# time complexity: O(n)

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        bought1 = bought2 = float('-inf')
        sold1 = sold2 = 0
        for p in prices:
            sold2 = max(sold2, bought2 + p)
            bought2 = max(bought2, sold1 - p)
            sold1 = max(sold1, bought1 + p)
            bought1 = max(bought1, -p)
        return sold2