# https://leetcode.com/problems/two-sum/
# time complexity: O(n)

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        encountered = {}
        for i, n in enumerate(nums):
            if target - n in encountered:
                return [encountered[target - n], i]
            encountered[n] = i