# https://leetcode.com/problems/fibonacci-number/description/

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n < 3:
            return 1

        a = b = 1

        for _ in range(n - 2):
            a, b = a + b, a

        return a
