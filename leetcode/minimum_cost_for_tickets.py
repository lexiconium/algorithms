# https://leetcode.com/problems/minimum-cost-for-tickets/

from functools import cache


class Solution:
    @cache
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        def dfs(index: int = 0, end: int = 0) -> int:
            if index == len(days):
                return 0

            min_dollors = float("inf")

            if (day := days[index]) < end:
                return dfs(index + 1, end)

            for cost, elongated in zip(costs, (1, 7, 30)):
                min_dollors = min(cost + dfs(index + 1, day + elongated), min_dollors)

            return min_dollors

        return dfs()

    # one of fastest solutions
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        last_day = max(days)
        days = set(days)

        dp = [0] * (last_day + 1)

        for day in range(1, last_day + 1):
            if day not in days:
                dp[day] = dp[day - 1]
                continue

            dp[day] = min(
                dp[day - 1] + costs[0],
                dp[max(day - 7, 0)] + costs[1],
                dp[max(day - 30, 0)] + costs[2],
            )

        return dp[-1]
