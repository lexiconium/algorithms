# https://leetcode.com/problems/partition-string-into-minimum-beautiful-substrings/


class Solution:
    # https://leetcode.com/problems/partition-string-into-minimum-beautiful-substrings/solutions/3737219/java-c-python-dp/
    def minimumBeautifulSubstrings(self, s: str) -> int:
        n = len(s)

        dp = [0] + [float("inf")] * n

        for i, c in enumerate(s):
            if c == "0":
                continue

            num = 0

            for j in range(i, n):
                if 15625 % (num := (num << 1) + (s[j] == "1")):
                    continue

                dp[j + 1] = min(dp[i] + 1, dp[j + 1])

        return dp[-1] if dp[-1] < float("inf") else -1
