# https://leetcode.com/problems/number-of-good-ways-to-split-a-string/description/

from collections import Counter


class Solution:
    def numSplits(self, s: str) -> int:
        cnt = 0

        left, right = Counter(), Counter(s)

        for c in s[:-1]:
            left[c] += 1
            right[c] -= 1

            if not right[c]:
                right.pop(c)

            cnt += len(left) == len(right)

        return cnt
