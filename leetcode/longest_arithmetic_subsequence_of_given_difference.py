# https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/

from collections import defaultdict


class Solution:
    # brute force
    def longestSubsequence(self, arr: list[int], difference: int) -> int:
        dp = [1] * (n := len(arr))

        for i in reversed(range(n - 1)):
            dp[i] = max(
                [1 + dp[j] for j in range(i + 1, n) if arr[j] - arr[i] == difference],
                default=1,
            )

        return max(dp)

    # dp
    def longestSubsequence(self, arr: list[int], difference: int) -> int:
        dp = defaultdict(int)
        longest = 1

        for n in reversed(arr):
            dp[n] = dp[n + difference] + 1
            longest = max(dp[n], longest)

        return longest
