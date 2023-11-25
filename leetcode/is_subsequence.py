# https://leetcode.com/problems/is-subsequence/description/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        i = 0

        for c in t:
            if c != s[i]:
                continue

            i += 1

            if i == len(s):
                return True

        return False
