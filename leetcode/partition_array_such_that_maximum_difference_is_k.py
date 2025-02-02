# https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/description/


class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        nums = sorted(nums)
        curr_min = nums[0]

        cnt = 1

        for n in nums:
            if n - curr_min > k:
                cnt += 1
                curr_min = n

        return cnt
