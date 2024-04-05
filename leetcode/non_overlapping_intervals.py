# https://leetcode.com/problems/non-overlapping-intervals/description/


class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals = sorted(intervals, key=lambda v: v[1])

        end = intervals[0][1]
        cnt = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                cnt += 1
                continue

            end = intervals[i][1]

        return cnt
