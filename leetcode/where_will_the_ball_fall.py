# https://leetcode.com/problems/where-will-the-ball-fall/

class Solution:
    def findBall(self, grid: list[list[int]]) -> list[int]:
        num_rows, num_cols = len(grid), len(grid[0])

        def valid(c: int) -> bool:
            return 0 <= c < num_cols

        def out(c: int) -> int:
            for r in range(num_rows):
                if not (valid(nc := c + grid[r][c]) and grid[r][nc] == grid[r][c]):
                    return -1

                c = nc

            return c

        return [out(c) for c in range(num_cols)]
