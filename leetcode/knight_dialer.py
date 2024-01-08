# https://leetcode.com/problems/knight-dialer/

from functools import cache


class Solution:
    def knightDialer(self, n: int) -> int:
        dp = [[0] * 10 for _ in range(n)]

        for num in range(10):
            dp[0][num] = 1

        num_pos = {0: (3, 1)}
        num_pos.update({num + 1: (num // 3, num % 3) for num in range(9)})

        def move_froms(num_to: int) -> list[int]:
            num_froms = []

            r_to, c_to = num_pos[num_to]

            for num_from in range(10):
                if num_from == num_to:
                    continue

                r_from, c_from = num_pos[num_from]

                if (d := (abs(r_to - r_from), abs(c_to - c_from))) != (2, 1) and d != (1, 2):
                    continue

                num_froms.append(num_from)

            return num_froms

        can_move = [move_froms(num) for num in range(10)]

        mod = int(1e9) + 7

        for m in range(n - 1):
            for num_to in range(10):
                dp[m + 1][num_to] = sum(
                    dp[m][num_from] % mod for num_from in can_move[num_to]
                ) % mod

        return sum(dp[-1]) % mod

    def knightDialer(self, n: int) -> int:
        can_move = {
            0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9],
            5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4]
        }

        mod = int(1e9) + 7

        @cache
        def dfs(n: int, num_to: int) -> int:
            if n == 0:
                return 1
            return sum(dfs(n - 1, num_from) for num_from in can_move[num_to]) % mod

        return sum(dfs(n, num_to) for num_to in range(10)) % mod
