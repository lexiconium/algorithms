# https://leetcode.com/problems/minimum-cost-to-make-all-characters-equal/description/


class Solution:
    def minimumCost(self, s: str) -> int:
        return sum(min(i, len(s) - i) for i in range(1, len(s)) if s[i - 1] != s[i])
