# https://leetcode.com/problems/champagne-tower/submissions/943127908/


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0 for _ in range(row + 1)] for row in range(query_row + 1)]
        dp[0][0] = poured

        for row in range(query_row):
            for col in range(row + 1):
                dp[row + 1][col] += (fall := max((dp[row][col] - 1) / 2, 0))
                dp[row + 1][col + 1] += fall

        return min(dp[query_row][query_glass], 1)
