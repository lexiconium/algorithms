# https://leetcode.com/problems/product-of-array-except-self/

# time complexity: O(n)

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        multiplied = []
        m = 1
        for n in nums:
            multiplied.append(m)
            m *= n
        m = 1
        for i in range(len(nums) - 1, -1, -1):
            multiplied[i] *= m
            m *= nums[i]
        return multiplied