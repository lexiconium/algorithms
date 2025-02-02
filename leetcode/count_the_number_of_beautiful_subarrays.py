# https://leetcode.com/problems/count-the-number-of-beautiful-subarrays/description/


import collections


class Solution:
    def beautifulSubarrays(self, nums: list[int]) -> int:
        prefix_xor = [0]
        cache = collections.Counter({0: 1})
        cnt = 0

        for n in nums:
            prefix_xor.append(xor := prefix_xor[-1] ^ n)
            cnt += cache[xor]
            cache[xor] += 1

        return cnt
