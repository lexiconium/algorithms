# https://leetcode.com/problems/maximum-product-difference-between-two-pairs/description/


class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:
        return (nums := sorted(nums))[-1] * nums[-2] - nums[1] * nums[0]
