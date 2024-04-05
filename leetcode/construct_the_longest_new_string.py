# https://leetcode.com/problems/construct-the-longest-new-string/description/


from functools import cache


class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        @cache
        def dfs(l: int, m: int, n: int, *, prev: str = "") -> int:
            if l == m == n == 0:
                return 0

            max_length = 0

            if prev != "A" and l:
                max_length = max(dfs(l - 1, m, n, prev="A") + 2, max_length)
            if prev != "B" and m:
                max_length = max(dfs(l, m - 1, n, prev="B") + 2, max_length)
            if prev != "A" and n:
                max_length = max(dfs(l, m, n - 1, prev="B") + 2, max_length)

            return max_length

        return dfs(x, y, z)

    def longestString(self, x: int, y: int, z: int) -> int:
        return 2 * (2 * min(x, y) + (x != y) + z)
