# https://leetcode.com/problems/maximum-alternating-subsequence-sum/description/


class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        sum_odd_comps = sum_even_comps = 0

        for n in nums:
            sum_odd_comps, sum_even_comps = (
                max(sum_even_comps + n, sum_odd_comps), max(sum_odd_comps - n, sum_even_comps)
            )

        return max(sum_odd_comps, sum_even_comps)

    # https://leetcode.com/problems/maximum-alternating-subsequence-sum/solutions/1298499/java-c-python-best-time-to-buy-and-sell-stock/
    def maxAlternatingSum(self, nums: list[int]) -> int:
        return nums[0] + sum(max(nums[i] - nums[i - 1], 0) for i in range(1, len(nums)))
