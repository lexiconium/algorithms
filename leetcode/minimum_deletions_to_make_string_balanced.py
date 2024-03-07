# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/description/


class Solution:
    def minimumDeletions(self, s: str) -> int:
        num_as = num_bs = 0

        for c in s:
            if c == "a":
                num_as = min(num_as + 1, num_bs)
            else:
                num_bs += 1

        return num_as
