# https://leetcode.com/problems/binary-trees-with-factors/


import bisect
from functools import cache


MOD = int(1e9) + 7


class Solution:
    def numFactoredBinaryTrees(self, arr: list[int]) -> int:
        arr = sorted(arr)
        nums = set(arr)

        @cache
        def dfs(node: int) -> int:
            if node not in nums:
                return 0

            return (
                sum(
                    [
                        dfs(arr[i]) * dfs(node // arr[i])
                        for i in range(bisect.bisect_left(arr, node))
                        if node % arr[i] == 0
                    ],
                    start=1,
                )
                % MOD
            )

        return sum(dfs(node) for node in arr) % MOD
