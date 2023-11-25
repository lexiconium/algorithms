# https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        dp = [[1] * n for n in range(1, numRows + 1)]

        for n in range(2, numRows):
            for m in range(1, n):
                dp[n][m] = dp[n - 1][m - 1] + dp[n - 1][m]

        return dp
