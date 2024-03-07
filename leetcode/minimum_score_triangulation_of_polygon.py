# https://leetcode.com/problems/minimum-score-triangulation-of-polygon/description/

from functools import cache


class Solution:
    # https://leetcode.com/problems/minimum-score-triangulation-of-polygon/solutions/286705/java-c-python-dp/
    def minScoreTriangulation(self, values: list[int]) -> int:
        @cache
        def dp(i: int, j: int) -> int:
            if j - i < 2:
                return 0
            return min(
                dp(i, k) + values[i] * values[k] * values[j] + dp(k, j)
                for k in range(i + 1, j)
            )

        return dp(0, len(values) - 1)
