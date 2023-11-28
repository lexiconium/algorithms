# https://leetcode.com/problems/generate-parentheses/

from functools import cache


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        @cache
        def dfs(l_remain: int, r_remain: int) -> list[str]:
            if not l_remain and not r_remain:
                return [""]

            pairs = []

            if l_remain:
                pairs.extend(["(" + p for p in dfs(l_remain - 1, r_remain)])

            if l_remain < r_remain:
                pairs.extend([")" + p for p in dfs(l_remain, r_remain - 1)])

            return pairs

        return dfs(n, n)
