# https://leetcode.com/problems/best-sightseeing-pair/description/


class Solution:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        max_score = max_before = 0

        for n in values:
            max_score = max(n + max_before, max_score)
            max_before = max(n, max_before) - 1

        return max_score
