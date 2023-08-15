# https://leetcode.com/problems/minimum-path-sum/submissions/

from functools import cache


class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @cache
        def min_sum(r: int, c: int) -> int:
            if r < 0 or c < 0:
                return float("inf")
            if r == 0 and c == 0:
                return grid[r][c]
            return min(min_sum(r - 1, c), min_sum(r, c - 1)) + grid[r][c]

        return min_sum(m - 1, n - 1)
