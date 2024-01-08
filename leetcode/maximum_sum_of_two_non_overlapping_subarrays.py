# https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/description/


class Solution:
    def maxSumTwoNoOverlap(self, nums: list[int], firstLen: int, secondLen: int) -> int:
        for i in range(len(nums) - 1):
            nums[i + 1] += nums[i]

        len_nums = len(nums)

        def dfs(target_len: int, begin: int = 0, end: int = len_nums) -> int:
            if target_len > end - begin:
                return -1
            return max(
                nums[i + target_len] - (nums[i] if i != -1 else 0)
                for i in range(begin - 1, end - target_len)
            )

        return max(
            max(dfs(firstLen, end=i) + dfs(secondLen, begin=i) for i in range(len(nums))),
            max(dfs(secondLen, end=i) + dfs(firstLen, begin=i) for i in range(len(nums)))
        )

    def maxSumTwoNoOverlap(self, nums: list[int], firstLen: int, secondLen: int) -> int:
        for i in range(len(nums) - 1):
            nums[i + 1] += nums[i]

        nums = [0] + nums

        def max_sum(len_left: int, len_right: int) -> int:
            max_left = max_total = 0

            for i in range(len(nums) - len_left - len_right):
                max_left = max(nums[j := i + len_left] - nums[i], max_left)
                max_total = max(max_left + nums[j + len_right] - nums[j], max_total)

            return max_total

        return max(max_sum(firstLen, secondLen), max_sum(secondLen, firstLen))
