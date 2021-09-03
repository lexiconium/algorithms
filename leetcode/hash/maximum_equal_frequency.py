# https://leetcode.com/problems/maximum-equal-frequency/
# https://leetcode.com/problems/maximum-equal-frequency/discuss/403743/JavaC%2B%2BPython-Only-2-Cases%3A-Delete-it-or-not

# time complexity: O(n)

import collections

class Solution:
    def maxEqualFreq(self, nums: list[int]) -> int:
        freq = collections.Counter()
        cnt = [0] * (len(nums) + 1)
        len_prefix = 0
        for i, n in enumerate(nums, 1):
            cnt[freq[n]] -= 1
            freq[n] += 1
            cnt[freq[n]] += 1
            if (len_eqs := cnt[freq[n]] * freq[n]) == i and i < len(nums):
                len_prefix = i + 1
            remainder = i - len_eqs
            if cnt[remainder] == 1 and remainder in [1, freq[n] + 1]:
                len_prefix = i
        return len_prefix