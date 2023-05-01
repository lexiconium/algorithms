# https://leetcode.com/problems/minimum-time-visiting-all-points/description/


class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        if (n := len(points)) == 1:
            return 0
        return sum(max(abs(e - b) for b, e in zip(points[i - 1], points[i])) for i in range(1, n))
