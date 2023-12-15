# https://leetcode.com/problems/airplane-seat-assignment-probability/description/


class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n == 1:
            return 1.0
        return 1 / n + (n - 2) * self.nthPersonGetsNthSeat(n - 1) / n

    # sum up
    def nthPersonGetsNthSeat(self, n: int) -> float:
        return 1.0 if n == 1 else 0.5
