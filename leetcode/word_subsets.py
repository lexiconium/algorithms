# https://leetcode.com/problems/word-subsets/description/


from collections import Counter
from functools import reduce


class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        max_occur_counter = reduce(lambda l, r: l | Counter(r), words2, Counter())
        return [a for a in words1 if Counter(a) & max_occur_counter == max_occur_counter]
