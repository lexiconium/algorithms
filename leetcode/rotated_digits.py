# https://leetcode.com/problems/rotated-digits/

INVALID, DEPENDENT, VALID = -1, 0, 1


class Solution:
    def rotatedDigits(self, n: int) -> int:
        dp = [
            DEPENDENT,
            DEPENDENT,
            VALID,
            INVALID,
            INVALID,
            VALID,
            VALID,
            INVALID,
            DEPENDENT,
            VALID,
        ]

        for m in range(len(dp), n + 1):
            str_m = str(m)
            first_digit, rest = int(str_m[0]), int(str_m[1:])

            f_validity = dp[first_digit]
            r_validity = dp[rest]

            if f_validity == INVALID or r_validity == INVALID:
                dp.append(INVALID)
            elif f_validity == DEPENDENT and r_validity == DEPENDENT:
                dp.append(DEPENDENT)
            else:
                dp.append(VALID)

        return sum(validity == VALID for validity in dp[: n + 1])
