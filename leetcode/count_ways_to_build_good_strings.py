# https://leetcode.com/problems/count-ways-to-build-good-strings/description/


MOD = int(1e9) + 7


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0] * (high + 1)
        dp[0] = 1

        for i in range(1, high + 1):
            dp[i] = (
                (dp[i - zero] if i >= zero else 0) + (dp[i - one] if i >= one else 0)
            ) % MOD

        return sum(dp[low : high + 1]) % MOD
