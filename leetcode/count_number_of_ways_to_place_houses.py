# https://leetcode.com/problems/count-number-of-ways-to-place-houses/description/


class Solution:
    def countHousePlacements(self, n: int) -> int:
        pprev, prev = 1, 1

        for _ in range(n):
            pprev, prev = prev, pprev + prev

        return pow(prev, 2, int(1e9) + 7)
