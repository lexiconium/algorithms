# https://leetcode.com/problems/count-numbers-with-unique-digits/description/


from functools import reduce


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        return 9 * reduce(
            lambda l, r: l * r, range(9, 9 - n + 1, -1), 1
        ) + self.countNumbersWithUniqueDigits(n - 1)
