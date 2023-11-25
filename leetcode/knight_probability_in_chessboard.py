# https://leetcode.com/problems/knight-probability-in-chessboard/description/


from functools import cache


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        def is_valid(r: int, c: int) -> bool:
            return 0 <= r < n and 0 <= c < n

        @cache
        def dfs(r: int, c: int, depth: int = 0) -> int:
            if not is_valid(r, c):
                return 0
            if depth == k:
                return 1

            return sum(
                dfs(r + dr, c + dc, depth + 1)
                for dr, dc in (
                    (-1, -2), (-2, -1), (-2, 1), (-1, 2),
                    (1, -2), (2, -1), (2, 1), (1, 2)
                )
            )

        return dfs(row, column) / 8**k
