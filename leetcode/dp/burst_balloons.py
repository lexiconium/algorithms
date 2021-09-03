# https://leetcode.com/problems/burst-balloons/
# https://leetcode.com/problems/burst-balloons/discuss/76228/Share-some-analysis-and-explanations

# time complexity:

class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        nums, n, N = [1] + nums + [1], len(nums), len(nums) + 2
        dp = [[0] * N for _ in range(N - 1)]
        for dist in range(2, N):
            for i in range(N - dist):
                k = i + dist
                dp[i][k] = max(dp[i][j] + nums[i] * nums[j] * nums[k] + dp[j][k]
                               for j in range(i + 1, k))
        return dp[0][n + 1]