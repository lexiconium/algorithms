# https://leetcode.com/problems/maximal-rectangle/
# https://leetcode.com/problems/maximal-rectangle/discuss/29065/AC-Python-DP-solutioin-120ms-based-on-largest-rectangle-in-histogram

# time complexity: O(n^2)

class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        _len = len(matrix[0])
        height = [0] * (_len + 1)
        _max = 0
        for row in matrix:
            for i in range(_len):
                height[i] = height[i] + 1 if row[i] == '1' else 0
            stack = [-1]
            for i in range(_len + 1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - stack[-1] - 1
                    _max = max(_max, h * w)
                stack.append(i)
        return _max