# https://leetcode.com/problems/minimum-falling-path-sum/description/


class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        for r in range(1, len(matrix)):
            for c in range(num_cols := len(matrix[0])):
                prev = matrix[r - 1][c]

                if c > 0:
                    prev = min(matrix[r - 1][c - 1], prev)

                if c + 1 < num_cols:
                    prev = min(matrix[r - 1][c + 1], prev)

                matrix[r][c] += prev

        return min(matrix[-1])
