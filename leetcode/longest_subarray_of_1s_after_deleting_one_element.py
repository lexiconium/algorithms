# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/


class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0

        ascending = nums[:]
        descending = nums[:]

        for i in range(1, len(ascending)):
            if not ascending[i]:
                continue

            ascending[i] += ascending[i - 1]

        for i in reversed(range(len(descending) - 1)):
            if not descending[i]:
                continue

            descending[i] += descending[i + 1]

        longest = max(descending[1], ascending[-2])

        for i in range(1, len(nums) - 1):
            longest = max(ascending[i - 1] + descending[i + 1], longest)

        return longest

    # https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/solutions/708112/java-c-python-sliding-window-at-most-one-0/
    def longestSubarray(self, nums: list[int]) -> int:
        num_remaining_removes, lidx = 1, 0

        for r in nums:
            num_remaining_removes -= r == 0

            if num_remaining_removes >= 0:
                continue

            num_remaining_removes += nums[lidx] == 0
            lidx += 1

        return len(nums) - lidx - 1
