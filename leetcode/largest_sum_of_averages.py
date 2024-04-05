# https://leetcode.com/problems/largest-sum-of-averages/

from functools import cache
from itertools import accumulate


class Solution:
    def largestSumOfAverages(self, nums: list[int], k: int) -> float:
        @cache
        def dfs(begin: int, end: int, n: int) -> int:
            if begin == end:
                return 0
            if end - begin == 1:
                return nums[begin]
            if n == 1:
                return sum(nums[begin:end]) / (end - begin)

            return max(
                dfs(begin, i, 1) + dfs(i, end, n - 1) for i in range(begin + 1, end)
            )

        return dfs(0, len(nums), k)

    def largestSumOfAverages(self, nums: list[int], k: int) -> float:
        n = len(nums)
        prefix_sums = list(accumulate(nums, initial=0))

        dp = [[0] * (n + 1) for _ in range(k)]

        for end in range(1, n + 1):
            dp[0][end] = prefix_sums[end] / end

        for group in range(1, k):
            for end in range(group, n + 1):
                dp[group][end] = max(
                    dp[group - 1][begin]
                    + (prefix_sums[end] - prefix_sums[begin]) / (end - begin)
                    for begin in range(end)
                )

        return dp[-1][-1]
