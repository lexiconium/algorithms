# https://leetcode.com/problems/sort-integers-by-the-power-value/description/

from functools import cache


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @cache
        def collatz(n: int) -> int:
            if n == 1:
                return 0

            if n % 2:
                return 1 + collatz(3 * n + 1)
            return 1 + collatz(n // 2)

        return sorted(list(range(lo, hi + 1)), key=lambda n: (collatz(n), n))[k - 1]
