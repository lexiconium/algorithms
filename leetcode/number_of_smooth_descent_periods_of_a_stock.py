# https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/description/


class Solution:
    def getDescentPeriods(self, prices: list[int]) -> int:
        p_prev = period = 0
        cnt = 0

        for p in prices:
            if p == p_prev - 1:
                period += 1
            else:
                period = 1

            cnt += period
            p_prev = p

        return cnt
