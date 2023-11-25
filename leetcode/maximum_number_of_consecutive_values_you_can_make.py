# https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/description/


class Solution:
    def getMaximumConsecutive(self, coins: list[int]) -> int:
        consecutive_sum = 0

        for coin in sorted(coins):
            if consecutive_sum + 1 < coin:
                return consecutive_sum + 1

            consecutive_sum += coin

        return consecutive_sum + 1
