# https://leetcode.com/problems/smallest-value-of-the-rearranged-number/description/


import bisect


class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return num

        if num < 0:
            digits = sorted(str(-num))
            return -int("".join(sorted(digits, reverse=True)))

        digits = sorted(str(num))
        first_nonzero_index = bisect.bisect_right(digits, "0")
        return int(
            "".join(
                [digits[first_nonzero_index]]
                + digits[:first_nonzero_index]
                + digits[first_nonzero_index + 1 :]
            )
        )
