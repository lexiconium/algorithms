# https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/

from functools import reduce


class Solution:
    def kthLargestValue(self, matrix: list[list[int]], k: int) -> int:
        dp = [[n for n in row] for row in matrix]

        for i, row in enumerate(matrix):
            for j, n in enumerate(row):
                if j == 0:
                    continue

                dp[i][j] ^= dp[i][j - 1]

        for i in range(len(dp)):
            if i == 0:
                continue

            for j in range(len(dp[0])):
                dp[i][j] ^= dp[i - 1][j]

        def concat(left: list, right: list) -> list:
            left.extend(right)
            return left

        return sorted(reduce(concat, dp, []))[-k]
