# https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/description/


from collections import deque


class Solution:
    def findMaxFish(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def in_bound(r: int, c: int) -> bool:
            return 0 <= r < m and 0 <= c < n

        def get_num_fish(r: int, c: int) -> int:
            q = deque([(r, c)])
            num_fish, grid[r][c] = grid[r][c], 0

            while q:
                r, c = q.popleft()

                for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                    if not in_bound(nr := r + dr, nc := c + dc):
                        continue
                    if not grid[nr][nc]:
                        continue

                    q.append((nr, nc))
                    num_fish += grid[nr][nc]
                    grid[nr][nc] = 0

            return num_fish

        max_num_fish = 0

        for r in range(m):
            for c in range(n):
                if not grid[r][c]:
                    continue

                max_num_fish = max(get_num_fish(r, c), max_num_fish)

        return max_num_fish
