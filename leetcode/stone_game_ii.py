# https://leetcode.com/problems/stone-game-ii/

from functools import cache


class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        @cache
        def dfs(index: int = 0, m: int = 1, alice: bool = True) -> tuple[int, int]:
            if index == len(piles):
                return 0, 0

            n = 0
            max_a = max_b = 0

            for x in range(min(2 * m, len(piles) - index)):
                n += piles[index + x]

                a, b = dfs(index + x + 1, max(x + 1, m), not alice)

                if alice and n + a > max_a:
                    max_a = n + a
                    max_b = b
                elif not alice and n + b > max_b:
                    max_a = a
                    max_b = n + b

            return max_a, max_b

        return dfs()[0]

    # https://leetcode.com/problems/stone-game-ii/solutions/345230/java-python-dp-solution/
    def stoneGameII(self, piles: list[int]) -> int:
        for i in reversed(range(len(piles) - 1)):
            piles[i] += piles[i + 1]

        @cache
        def dfs(index: int = 0, m: int = 1) -> int:
            if index + 2 * m >= len(piles):
                return piles[index]
            return piles[index] - min(dfs(index + x, max(x, m)) for x in range(1, 2 * m + 1))

        return dfs()
