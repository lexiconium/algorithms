# https://leetcode.com/problems/longest-increasing-subsequence/


import bisect


class Solution:
    # brute force
    def lengthOfLIS(self, nums: list[int]) -> int:
        def dfs(begin: int, n: int) -> int:
            if begin == len(nums):
                return 0

            cnt = 0

            for i in range(begin, len(nums)):
                if nums[i] <= n:
                    continue

                cnt = max(1 + dfs(i + 1, nums[i]), cnt)

            return cnt

        return dfs(0, float("-inf"))

    # dp
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * (n := len(nums))

        for i in reversed(range(n - 1)):
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    dp[i] = max(1 + dp[j], dp[i])

        return max(dp)

    # binary search
    def lengthOfLIS(self, nums: list[int]) -> int:
        tails = []

        for n in nums:
            if (index := bisect.bisect_left(tails, n)) == len(tails):
                tails.append(n)
            else:
                tails[index] = n

        return len(tails)
