# https://leetcode.com/problems/maximum-compatibility-score-sum/

from functools import cache


class Solution:
    def maxCompatibilitySum(self, students: list[list[int]], mentors: list[list[int]]) -> int:
        def compat_score(student: list[int], mentor: list[int]) -> list[int]:
            return sum(l == r for l, r in zip(student, mentor))

        compatibility_scores = [
            [compat_score(student, mentor) for mentor in mentors]
            for student in students
        ]

        m = len(students)

        @cache
        def dfs(i: int = 0, unavailable: int = 0) -> int:
            if i == m:
                return 0

            return max(
                compatibility_scores[i][j] + dfs(i + 1, unavailable | (1 << j))
                for j in range(m)
                if not unavailable & (1 << j)
            )

        return dfs()
