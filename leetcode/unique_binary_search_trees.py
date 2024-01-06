# https://leetcode.com/problems/unique-binary-search-trees/description/

from functools import cache


class Solution:
    @cache
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1

        return sum(
            self.numTrees(m) * self.numTrees(n - 1 - m)
            for m in range(n)
        )
