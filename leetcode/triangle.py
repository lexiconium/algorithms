# https://leetcode.com/problems/triangle/


class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        for i in range(1, len(triangle)):
            for j in range(i + 1):
                triangle[i][j] += min(
                    triangle[i - 1][j - 1] if j > 0 else float("inf"),
                    triangle[i - 1][j] if j < i else float("inf"),
                )

        return min(triangle[-1])

    def minimumTotal(self, triangle: list[list[int]]) -> int:
        for i in reversed(range(len(triangle) - 1)):
            for j in range(i + 1):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])

        return triangle[0][0]
