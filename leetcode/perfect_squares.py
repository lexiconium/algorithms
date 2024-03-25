# https://leetcode.com/problems/perfect-squares/


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        for m in range(1, n + 1):
            for l in range(1, int(m**0.5) + 1):
                dp[m] = min(dp[m - l**2] + 1, dp[m])

        return dp[-1]
