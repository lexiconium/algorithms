# https://leetcode.com/problems/delete-operation-for-two-strings/description/


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        for i, c1 in enumerate(word1, 1):
            for j, c2 in enumerate(word2, 1):
                if c1 == c2:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return len(word1) + len(word2) - 2 * dp[-1][-1]
