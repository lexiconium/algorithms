# https://leetcode.com/problems/integer-break/description/

from functools import cache


class Solution:
    @cache
    def integerBreak(self, n: int) -> int:
        if n == 1:
            return 1
        return max(
            max(self.integerBreak(m), m) * max(self.integerBreak(n - m), n - m)
            for m in range(1, n // 2 + 1)
        )
