# https://leetcode.com/problems/edit-distance/


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        for r in range(len(word1) + 1):
            dp[r][0] = r

        for c in range(len(word2) + 1):
            dp[0][c] = c

        for l, c1 in enumerate(word1, 1):
            for m, c2 in enumerate(word2, 1):
                if c1 == c2:
                    dp[l][m] = dp[l - 1][m - 1]
                else:
                    dp[l][m] = min(dp[l - 1][m - 1], dp[l - 1][m], dp[l][m - 1]) + 1

        return dp[-1][-1]
