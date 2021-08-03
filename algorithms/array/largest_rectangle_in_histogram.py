# https://leetcode.com/problems/largest-rectangle-in-histogram/
# https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28917/AC-Python-clean-solution-using-stack-76ms

# time complexity: O(n)

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        heights.append(0)
        stack = [-1]
        _max = 0
        for i, h_i in enumerate(heights):
            while h_i < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                _max = max(_max, h * w)
            stack.append(i)
        return _max