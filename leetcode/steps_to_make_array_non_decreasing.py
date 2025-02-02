# https://leetcode.com/problems/steps-to-make-array-non-decreasing/description/


class Solution:
    def totalSteps(self, nums: list[int]) -> int:
        dp, stack = [0] * len(nums), []

        for i in reversed(range(len(nums))):
            while stack and nums[i] > nums[stack[-1]]:
                dp[i] = max(dp[i] + 1, dp[stack.pop()])
            stack.append(i)

        return max(dp)
