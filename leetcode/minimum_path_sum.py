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

    def minPathSum(self, grid: list[list[int]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])

        def getitem(r: int, c: int) -> int | float:
            if 0 <= r < num_rows and 0 <= c < num_cols:
                return grid[r][c]
            return float("inf")

        for r in range(num_rows):
            for c in range(num_cols):
                if r == c == 0:
                    continue

                grid[r][c] += min(getitem(r - 1, c), getitem(r, c - 1))

        return grid[-1][-1]
