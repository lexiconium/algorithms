# https://leetcode.com/problems/soup-servings/description/


class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 4800:
            return 1

        @cache
        def dfs(l: int, m: int) -> int | float:
            if l == 0 and m > 0:
                return 1
            if l == m == 0:
                return 0.5
            if l > 0 and m == 0:
                return 0

            return 0.25 * sum(
                [
                    dfs(max(l - 100, 0), m),
                    dfs(max(l - 75, 0), max(m - 25, 0)),
                    dfs(max(l - 50, 0), max(m - 50, 0)),
                    dfs(max(l - 25, 0), max(m - 75, 0)),
                ]
            )

        return dfs(n, n)
