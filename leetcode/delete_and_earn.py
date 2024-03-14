# https://leetcode.com/problems/delete-and-earn/description/

from collections import Counter


class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        nums_cnt = Counter(nums)
        max_num = max(nums_cnt.keys())

        dp = [0] * (max_num + 1)
        dp[1] = nums_cnt[1]

        for n in range(2, max_num + 1):
            dp[n] = max(n * nums_cnt[n] + dp[n - 2], dp[n - 1])

        return dp[max_num]
