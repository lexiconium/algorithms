# https://leetcode.com/problems/beautiful-arrangement/description/

from functools import cache


class Solution:
    def countArrangement(self, n: int) -> int:
        @cache
        def dfs(m: int, occupied: int = 0) -> int:
            if m == 0:
                return 1

            return sum(
                dfs(m - 1, occupied | (1 << l)) for l in range(n)
                if not occupied & (1 << l) and (m % (l + 1) == 0 or (l + 1) % m == 0)
            )

        return dfs(n)
