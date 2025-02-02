# https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/description/

import bisect
import itertools


class Solution:
    def chalkReplacer(self, chalk: list[int], k: int) -> int:
        k %= sum(chalk)

        for i, m in enumerate(chalk):
            if k < m:
                return i
            k -= m

    def chalkReplacer(self, chalk: list[int], k: int) -> int:
        return bisect.bisect_right(list(itertools.accumulate(chalk)), k % sum(chalk))
