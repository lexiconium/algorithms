# https://leetcode.com/problems/2-keys-keyboard/description/


class Solution:
    def minSteps(self, n: int) -> int:
        dp = [0] * (n + 1)

        for m in range(2, n + 1):
            for l in reversed(range(1, m)):
                if m % l:
                    continue

                dp[m] = dp[l] + m // l
                break

        return dp[-1]
