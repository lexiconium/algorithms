# https://leetcode.com/problems/find-the-divisibility-array-of-a-string/description/


class Solution:
    def divisibilityArray(self, word: str, m: int) -> list[int]:
        divarr = []
        remainder = 0

        for n in map(int, word):
            if remainder := (10 * remainder + n) % m:
                divarr.append(0)
            else:
                divarr.append(1)

        return divarr
