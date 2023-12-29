# https://leetcode.com/problems/ways-to-make-a-fair-array/


class Solution:
    def waysToMakeFair(self, nums: list[int]) -> int:
        nums = [0] + nums

        for i in range(1, len(nums)):
            nums[i] *= (-1 if i % 2 else 1)
            nums[i] += nums[i - 1]

        return sum(
            nums[-1] - nums[i] == nums[i - 1]
            for i in range(1, len(nums))
        )
