# https://leetcode.com/problems/trapping-rain-water/

# time complexity: O(n)

class Solution:
    def trap(self, height: list[int]) -> int:
        if len(height) < 3:
            return 0
        
        left_max = height[(left := 0)]
        right_max = height[(right := len(height) - 1)]
        volume = 0
        while left < right:
            if left_max < right_max:
                volume += left_max - height[left]
                left += 1
                left_max = max(left_max, height[left])
            else:
                volume += right_max - height[right]
                right -= 1
                right_max = max(right_max, height[right])
        return volume