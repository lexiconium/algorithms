# https://leetcode.com/problems/minimum-index-of-a-valid-split/


import collections


class Solution:
    def minimumIndex(self, nums: list[int]) -> int:
        counter = collections.Counter(nums)
        num, cnt = counter.most_common(1)[0]

        if cnt * 2 < (length := len(nums)):
            return -1

        cur_cnt = 0

        for l, n in enumerate(nums, 1):
            cur_cnt += n == num

            if cur_cnt * 2 > l and (cnt - cur_cnt) * 2 > length - l:
                return l - 1

        return -1
