# https://leetcode.com/problems/maximal-square/discuss/600149/Python-Thinking-Process-Diagrams-DP-Approach

# time complexity: O(mn)

class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        max_side = 0
        
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == '1':
                    dp[row + 1][col + 1] = min(dp[row][col], dp[row + 1][col], dp[row][col + 1]) + 1
                    max_side = max(max_side, dp[row + 1][col + 1])
        
        return max_side ** 2