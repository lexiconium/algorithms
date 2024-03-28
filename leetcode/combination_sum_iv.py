# https://leetcode.com/problems/combination-sum-iv/description/

from functools import cache


class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        @cache
        def dfs(target: int) -> int:
            if target == 0:
                return 1
            return sum(dfs(target - n) for n in nums if n <= target)

        return dfs(target)

    def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        for t in range(1, target + 1):
            dp[t] = sum(dp[t - n] for n in nums if n <= t)

        return dp[-1]
