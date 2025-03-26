# https://leetcode.com/problems/number-of-ways-to-earn-points/description/


class Solution:
    def waysToReachTarget(self, target: int, types: list[list[int]]) -> int:
        dp = [1] + [0] * target
        mod = int(1e9) + 7

        for cnt, mark in types:
            # To avoid using updated values within the same iteration, iterate in reverse order.
            for sub_target in reversed(range(target + 1)):
                for n in range(1, min(cnt, sub_target // mark) + 1):
                    dp[sub_target] += dp[sub_target - mark * n]
                    dp[sub_target] %= mod

        return dp[-1]
