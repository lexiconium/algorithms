# https://leetcode.com/problems/palindrome-partitioning/

from functools import cache


class Solution:
    @cache
    def partition(self, s: str) -> list[list[str]]:
        if not s:
            return [[]]

        subs = []

        for i in range(1, len(s) + 1):
            if (left := s[:i]) != left[::-1]:
                continue

            for right in self.partition(s[i:]):
                subs.append([left] + right)

        return subs
