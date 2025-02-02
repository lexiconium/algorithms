# https://leetcode.com/problems/extra-characters-in-a-string


class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        dictionary = set(dictionary)
        dp = [float("inf")] * (len_str := len(s)) + [0]

        for i in reversed(range(len_str)):
            for j in range(i + 1, len_str + 1):
                if (substr := s[i:j]) in dictionary:
                    dp[i] = min(dp[j], dp[i])
                else:
                    dp[i] = min(len(substr) + dp[j], dp[i])

        return dp[0]
