# https://leetcode.com/problems/intersection-of-multiple-arrays/description/


class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        intersection = set(nums[0])

        for arr in nums[1:]:
            intersection &= set(arr)

        return sorted(intersection)
