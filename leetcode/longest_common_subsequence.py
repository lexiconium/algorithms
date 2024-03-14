# https://leetcode.com/problems/longest-common-subsequence/description/


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for i, c1 in enumerate(text1, 1):
            for j, c2 in enumerate(text2, 1):
                dp[i][j] = (
                    dp[i - 1][j - 1] + 1
                    if c1 == c2
                    else max(dp[i - 1][j], dp[i][j - 1])
                )

        return dp[-1][-1]
