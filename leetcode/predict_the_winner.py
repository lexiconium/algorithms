# https://leetcode.com/problems/predict-the-winner/description/


class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        n = len(nums)
        dp = [[0] * n for _ in nums]

        for i, num in enumerate(nums):
            dp[i][i] = num

        for i in reversed(range(n - 1)):
            for j in range(i + 1, n):
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])

        return dp[0][-1] >= 0
