# https://leetcode.com/problems/four-divisors/submissions/943173970/

from collections import defaultdict


class Solution:
    def sumFourDivisors(self, nums: list[int]) -> int:
        divisors = defaultdict(set)
        divisors_sums = defaultdict(int)
        divisors_sum = 0

        for n in nums:
            if n in divisors and len(divisors[n]) == 4:
                divisors_sum += divisors_sums[n]
                continue

            for m in range(1, int(n ** (1 / 2) + 1)):
                div, mod = divmod(n, m)
                if mod == 0:
                    divisors[n] |= {div, m}

            divisors_sums[n] = sum(divisors[n])

            if len(divisors[n]) == 4:
                divisors_sum += divisors_sums[n]

        return divisors_sum
