# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/

from functools import cache


class Solution:
    # TLE
    @cache
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        if not s1 or not s2:
            return float("inf")

        if s1 == s2:
            return 0

        return min(
            min(
                ord(c1) + self.minimumDeleteSum(s1[:i] + s1[i + 1:], s2)
                for i, c1 in enumerate(s1)
            ),
            min(
                ord(c2) + self.minimumDeleteSum(s1, s2[:j] + s2[j + 1:])
                for j, c2 in enumerate(s2)
            ),
            min(
                ord(c1) + ord(c2) + self.minimumDeleteSum(s1[:i] + s1[i + 1:], s2[:j] + s2[j + 1:])
                for i, c1 in enumerate(s1)
                for j, c2 in enumerate(s2)
            )
        )

    # https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/solutions/642422/for-those-who-have-no-clue-step-by-step/
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

        for j, c2 in enumerate(s2):
            dp[0][j + 1] = dp[0][j] + ord(c2)

        for i, c1 in enumerate(s1):
            dp[i + 1][0] = dp[i][0] + ord(c1)

            for j, c2 in enumerate(s2):
                if c1 == c2:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = min(
                        dp[i][j + 1] + ord(c1), dp[i + 1][j] + ord(c2)
                    )

        return dp[-1][-1]
