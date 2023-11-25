# https://leetcode.com/problems/koko-eating-bananas/description/

from math import ceil


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        min_k, max_k = 1, max(piles)

        while min_k < max_k:
            k = (min_k + max_k) // 2
            time_takes = sum(ceil(num_bananas / k) for num_bananas in piles)

            if time_takes <= h:
                max_k = k
            else:
                min_k = k + 1

        return min_k
