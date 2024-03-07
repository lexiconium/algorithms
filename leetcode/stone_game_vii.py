# https://leetcode.com/problems/stone-game-vii/description/

from itertools import accumulate


class Solution:
    def stoneGameVII(self, stones: list[int]) -> int:
        prefix_sums = list(accumulate(stones, initial=0))

        dp = [[0] * len(stones) for _ in stones]

        for i in reversed(range(len(stones) - 1)):
            for j in range(i + 1, len(stones)):
                dp[i][j] = max(
                    prefix_sums[j + 1] - prefix_sums[i + 1] - dp[i + 1][j],
                    prefix_sums[j] - prefix_sums[i] - dp[i][j - 1],
                )

        return dp[0][-1]
