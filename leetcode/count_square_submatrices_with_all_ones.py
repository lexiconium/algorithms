# https://leetcode.com/problems/count-square-submatrices-with-all-ones/description/

class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        cnt = 0

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if not matrix[r][c]:
                    continue

                if r and c:
                    matrix[r][c] += min(matrix[r][c - 1], matrix[r - 1][c - 1], matrix[r - 1][c])

                cnt += matrix[r][c]

        return cnt
