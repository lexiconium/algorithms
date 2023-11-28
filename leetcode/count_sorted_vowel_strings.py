# https://leetcode.com/problems/count-sorted-vowel-strings/description/

class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [1] * 5

        for m in range(1, n):
            tmp = [0] * 5

            for i in range(5):
                tmp[i] = sum(dp[j] for j in range(i + 1))

            dp = tmp

        return sum(dp)
