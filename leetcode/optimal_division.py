# https://leetcode.com/problems/optimal-division/description/


class Solution:
    def optimalDivision(self, nums: list[int]) -> str:
        if len(nums) < 3:
            return "/".join(map(str, nums))
        return f"{nums[0]}/({'/'.join(map(str, nums[1:]))})"
