# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/

# time complexity: O(n)

class Solution:
    def maxSumOfThreeSubarrays(self, nums: list[int], k: int) -> list[int]:
        window1, window2, window3 = sum(nums[:k]), sum(nums[k:2 * k]), sum(nums[2 * k:3 * k])
        max1, max2, max3 = window1, window1 + window2, window1 + window2 + window3
        idx1, idx2, idx3 = 0, [0, k], [0, k, 2 * k]
        
        for i in range(k, len(nums) - 2 * k):
            window1 += nums[i] - nums[i - k]
            if window1 > max1:
                max1 = window1
                idx1 = i - k + 1
            
            window2 += nums[i + k] - nums[i]
            if max1 + window2 > max2:
                max2 = max1 + window2
                idx2 = [idx1, i + 1]
            
            window3 += nums[i + 2 * k] - nums[i + k]
            if max2 + window3 > max3:
                max3 = max2 + window3
                idx3 = idx2 + [i + k + 1]
                
        return idx3