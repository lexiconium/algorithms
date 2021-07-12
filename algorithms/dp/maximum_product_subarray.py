# https://leetcode.com/problems/maximum-product-subarray/
# https://leetcode.com/problems/maximum-product-subarray/discuss/183483/JavaC%2B%2BPython-it-can-be-more-simple

# time complexity: O(n)

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        rev_nums = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            rev_nums[i] *= rev_nums[i - 1] or 1
        return max(nums + rev_nums)