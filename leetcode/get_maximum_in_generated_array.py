# https://leetcode.com/problems/get-maximum-in-generated-array/description/

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n < 2:
            return n

        dp = [0] * (n + 1)
        dp[1] = 1

        for m in range(2, n + 1):
            dp[m] = dp[m // 2]

            if m % 2:
                dp[m] += + dp[m // 2 + 1]

        return max(dp)
