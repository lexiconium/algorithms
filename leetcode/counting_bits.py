# https://leetcode.com/problems/counting-bits

class Solution:
    def countBits(self, n: int) -> list[int]:
        dp = [0] * (n + 1)

        for m in range(1, n + 1):
            dp[m] = dp[m >> 1] + (m & 1)

        return dp
