# https://leetcode.com/problems/arithmetic-slices/description/


class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        d = float("inf")
        length = 1

        cnt = 0

        for i in range(1, len(nums)):
            if (nd := nums[i] - nums[i - 1]) != d:
                cnt += (length - 2) * (length - 1) // 2

                d = nd
                length = 2
            else:
                length += 1

        return cnt + (length - 2) * (length - 1) // 2

    # simplified
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        num_comps = cnt = 0

        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                num_comps += 1
            else:
                num_comps = 0

            cnt += num_comps

        return cnt
