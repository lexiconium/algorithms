# https://leetcode.com/problems/patching-array/description/


class Solution:
    def minPatches(self, nums: list[int], n: int) -> int:
        consec_sum, cnt = 0, 0

        for num in nums:
            while num > consec_sum + 1:
                consec_sum += consec_sum + 1
                cnt += 1

                if consec_sum >= n:
                    return cnt

            consec_sum += num

            if consec_sum >= n:
                return cnt

        while consec_sum < n:
            consec_sum += consec_sum + 1
            cnt += 1

        return cnt
