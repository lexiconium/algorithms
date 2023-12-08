# https://leetcode.com/problems/palindromic-substrings/description/


class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[0] * len(s) for _ in s]

        for i in reversed(range(len(s))):
            dp[i][i] = 1

            for j in range(i + 1, len(s)):
                dp[i][j] = (s[i] == s[j]) * (dp[i + 1][j - 1] or j == i + 1)

        return sum(sum(row) for row in dp)
