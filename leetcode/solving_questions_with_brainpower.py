# https://leetcode.com/problems/solving-questions-with-brainpower/


class Solution:
    # brute force
    def mostPoints(self, questions: list[list[int]]) -> int:
        def dfs(i: int = 0) -> int:
            if i >= len(questions):
                return 0

            return max(questions[i][0] + dfs(i + 1 + questions[i][1]), dfs(i + 1))

        return dfs()

    # tabulation
    def mostPoints(self, questions: list[list[int]]) -> int:
        dp = [0] * (n := len(questions))

        for i in reversed(range(n)):
            p, bp = questions[i]
            dp[i] = max(
                p + (dp[i + 1 + bp] if i + 1 + bp < n else 0),
                dp[i + 1] if i + 1 < n else 0,
            )

        return dp[0]
