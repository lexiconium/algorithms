# https://leetcode.com/problems/count-of-smaller-numbers-after-self/

# time complexity: O(n^2)

import bisect

class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        cnt, tmp = [], []
        for n in nums[::-1]:
            i = bisect.bisect_left(tmp, n)
            tmp.insert(i, n)
            cnt.append(i)
        return cnt[::-1]