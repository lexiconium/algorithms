# https://leetcode.com/problems/coin-change-ii/description/


class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]

        for i in range(len(coins)):
            dp[i + 1][0] = 1

        for i, coin in enumerate(coins):
            for target in range(1, amount + 1):
                dp[i + 1][target] += dp[i][target]

                if target < coin:
                    continue

                dp[i + 1][target] += dp[i + 1][target - coin]

        return dp[-1][-1]
