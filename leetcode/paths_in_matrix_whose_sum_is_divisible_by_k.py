# https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/description/


class Solution:
    def numberOfPaths(self, grid: list[list[int]], k: int) -> int:
        dp = [[[0 for _ in range(k)] for _ in row] for row in grid]
        dp[0][0][grid[0][0] % k] = 1

        mod = int(1e9) + 7

        for r, row in enumerate(grid):
            for c, n in enumerate(row):
                for m in range(k):
                    path_mod = (m + n) % k

                    if r:
                        dp[r][c][path_mod] += dp[r - 1][c][m]
                    if c:
                        dp[r][c][path_mod] += dp[r][c - 1][m]

                    dp[r][c][path_mod] %= mod

        return dp[-1][-1][0]
