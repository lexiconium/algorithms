# https://leetcode.com/problems/find-good-days-to-rob-the-bank/description/


import collections


class Solution:
    def goodDaysToRobBank(self, security: list[int], time: int) -> list[int]:
        num_days = len(security)

        def _security(i: int) -> float | int:
            if 0 <= i < num_days:
                return security[i]
            return float("inf")

        non_inc_cache = collections.Counter()
        non_dec_cache = collections.Counter()

        for i in reversed(range(num_days)):
            if security[i] <= _security(i + 1):
                non_dec_cache[i] = non_dec_cache[i + 1] + 1
            else:
                non_dec_cache[i] = 1

        days = []

        for i in range(num_days):
            if security[i] <= _security(i - 1):
                non_inc_cache[i] = non_inc_cache[i - 1] + 1
            else:
                non_inc_cache[i] = 1

            if non_inc_cache[i] > time and non_dec_cache[i] > time:
                days.append(i)

        return days
