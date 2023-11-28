# https://leetcode.com/problems/partition-array-for-maximum-sum/

class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        dp = [0] * (len(arr) + 1)

        for end in range(1, len(arr) + 1):
            n = float("-inf")

            for prev_end in reversed(range(max(end - k, 0), end)):
                n = max(arr[prev_end], n)
                dp[end] = max(dp[prev_end] + n * (end - prev_end), dp[end])

        return dp[-1]
