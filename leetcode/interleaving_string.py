# https://leetcode.com/problems/interleaving-string/description/

from functools import cache

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        @cache
        def dfs(idx1: int = 0, idx2: int = 0) -> bool:
            if idx1 == len(s1) and idx2 == len(s2):
                return True

            f = False

            if idx1 < len(s1) and s1[idx1] == s3[idx1 + idx2]:
                f = dfs(idx1 + 1, idx2)

            if f:
                return True

            if idx2 < len(s2) and s2[idx2] == s3[idx1 + idx2]:
                f = dfs(idx1, idx2 + 1)

            return f

        return dfs()
