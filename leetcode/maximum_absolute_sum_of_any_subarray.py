# https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/description/


from itertools import accumulate


class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        prefix = 0
        max_abs_sum = 0

        smallest = largest = 0

        for n in nums:
            prefix += n

            if prefix > smallest:
                max_abs_sum = max(prefix - smallest, max_abs_sum)
                largest = max(prefix, largest)

            if prefix < largest:
                max_abs_sum = max(largest - prefix, max_abs_sum)
                smallest = min(prefix, smallest)

        return max_abs_sum

    def maxAbsoluteSum(self, nums: list[int]) -> int:
        return max(accumulate(nums, initial=0)) - min(accumulate(nums, initial=0))
