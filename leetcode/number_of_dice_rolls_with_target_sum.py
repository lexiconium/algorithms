# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if target < n:
            return 0

        dp = [[0] * (max(target, k) + 1) for _ in range(n)]
        mod = int(1e9) + 7

        for t in range(1, k + 1):
            dp[0][t] = 1

        for m in range(1, n):
            for t in range(1, target + 1):
                dp[m][t] = sum(
                    dp[m - 1][t - l] % mod for l in range(1, k + 1)
                    if t - l > 0
                ) % mod

        return dp[-1][target]
