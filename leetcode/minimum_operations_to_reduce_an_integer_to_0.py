# https://leetcode.com/problems/minimum-operations-to-reduce-an-integer-to-0/description/


class Solution:
    def minOperations(self, n: int) -> int:
        cnt = 0

        while n:
            if n % 2 == 0:
                n >>= 1

            # if preceding 1 exists, add 1
            # even if there is only one preceding 1, count will be same;
            # subtracting 1 twice or add 1 to subtract 1 once
            elif n & 2:
                n += 1
                cnt += 1

            # isolated 1
            else:
                n >>= 2
                cnt += 1

        return cnt
