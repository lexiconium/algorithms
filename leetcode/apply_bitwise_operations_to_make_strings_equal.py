# https://leetcode.com/problems/apply-bitwise-operations-to-make-strings-equal/description/


class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        return ("1" in s) == ("1" in target)
