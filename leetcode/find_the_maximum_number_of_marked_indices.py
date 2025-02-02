# https://leetcode.com/problems/find-the-maximum-number-of-marked-indices/description/


class Solution:
    def maxNumOfMarkedIndices(self, nums: list[int]) -> int:
        nums = sorted(nums)
        half = len(nums) // 2
        i, j = half - 1, len(nums) - 1
        cnt = 0

        while 0 <= i and half <= j:
            if nums[i] * 2 <= nums[j]:
                j -= 1
                cnt += 2

            i -= 1

        return cnt
