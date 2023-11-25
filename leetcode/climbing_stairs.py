# https://leetcode.com/problems/climbing-stairs/description/

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        a, b = 1, 2

        for _ in range(n - 2):
            b, a = a + b, b

        return b
