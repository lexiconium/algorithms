# https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n < 3:
            return 1

        a, b, c = 0, 1, 1

        for _ in range(3, n + 1):
            c, b, a = a + b + c, c, b

        return c
