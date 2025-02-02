# https://leetcode.com/problems/count-nice-pairs-in-an-array/description/


import collections


class Solution:
    def countNicePairs(self, nums: list[int]) -> int:
        counter = collections.defaultdict(int)
        cnt = 0

        for n in reversed(nums):
            cnt += counter[diff := n - int(str(n)[::-1])]
            counter[diff] += 1

        return cnt % (int(1e9) + 7)
