# https://leetcode.com/problems/extra-characters-in-a-string/description/


class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        dp = [0] + [float("inf")] * (n := len(s))
        dictionary = set(dictionary)

        for end in range(1, n + 1):
            dp[end] = min(
                dp[begin] + (end - begin) * (s[begin:end] not in dictionary)
                for begin in range(end)
            )

        return dp[-1]
