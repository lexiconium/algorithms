# https://leetcode.com/problems/minimum-operations-to-make-array-equal/description/


class Solution:
    def minOperations(self, n: int) -> int:
        # odd:
        # make equal to 2 * (n // 2) + 1 = n
        # [sum from 0 to (n - 1) / 2] * 2 = (n - 1) * (n + 1) / 4
        # = (n ** 2 - 1) / 4 = n ** 2 // 4

        # even:
        # make equal to n
        # [sum from 0 to n - 1] - [sum from 0 to (n - 2) / 2] * 2
        # = (n - 1) * n / 2 - (n - 2) * n / 4 = n ** 2 / 4

        return n**2 // 4
