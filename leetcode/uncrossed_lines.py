# https://leetcode.com/problems/uncrossed-lines/

from collections import defaultdict
from functools import cache


class Solution:
    def maxUncrossedLines(self, nums1: list[int], nums2: list[int]) -> int:
        n2lidx = defaultdict(list)

        for i, n in enumerate(nums2):
            n2lidx[n].append(i)

        @cache
        def dfs(uidx: int = 0, lidx: int = 0) -> int:
            if uidx == len(nums1) or lidx == len(nums2):
                return 0

            num_connections = dfs(uidx + 1, lidx)

            if (n := nums1[uidx]) not in n2lidx:
                return num_connections

            for nlidx in n2lidx[n]:
                if nlidx < lidx:
                    continue

                return max(dfs(uidx + 1, nlidx + 1) + 1, num_connections)

            return num_connections

        return dfs()
