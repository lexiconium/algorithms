# https://leetcode.com/problems/count-unguarded-cells-in-the-grid/


import collections


class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]
    ) -> int:
        guarded = [[0] * n for _ in range(m)]

        for r, c in guards:
            guarded[r][c] = (1 << 5) - 1

        for r, c in walls:
            guarded[r][c] = (1 << 5) - 1

        dp = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def in_bound(r: int, c: int) -> bool:
            return 0 <= r < m and 0 <= c < n

        for gr, gc in guards:
            q = collections.deque([(gr, gc, d) for d in range(4)])

            while q:
                r, c, d = q.popleft()
                dr, dc = dp[d]

                if not in_bound(nr := r + dr, nc := c + dc):
                    continue
                if guarded[nr][nc] & 1 << d:
                    continue

                guarded[nr][nc] |= 1 << d
                q.append((nr, nc, d))

        return sum(len(list(filter(lambda v: v == 0, row))) for row in guarded)
