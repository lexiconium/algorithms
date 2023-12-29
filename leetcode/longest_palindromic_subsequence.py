# https://leetcode.com/problems/longest-palindromic-subsequence/description/


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0] * len(s) for _ in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = 1

        for i in reversed(range(len(s) - 1)):
            for j in range(i + 1, len(s)):
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

                if s[i] == s[j]:
                    dp[i][j] = max(dp[i + 1][j - 1] + 2, dp[i][j])

        return dp[0][-1]
