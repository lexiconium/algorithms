# https://leetcode.com/problems/flip-string-to-monotone-increasing/description/


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        num_right_flips = [int(b == "0") for b in s] + [0]

        for i in reversed(range(len(s))):
            num_right_flips[i] += num_right_flips[i + 1]

        num_left_flips = [0] + [int(b == "1") for b in s]

        for i in range(len(s)):
            num_left_flips[i + 1] += num_left_flips[i]

        return min(
            num_left_flips[i] + num_right_flips[i]
            for i in range(len(s) + 1)
        )

    def minFlipsMonoIncr(self, s: str) -> int:
        num_ones = num_flips = 0

        for b in s:
            if b == "1":
                num_ones += 1
            else:
                num_flips += 1

                if num_flips > num_ones:
                    num_flips = num_ones

        return num_flips
