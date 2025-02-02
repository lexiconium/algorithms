# https://leetcode.com/problems/maximum-split-of-positive-even-integers/description/


class Solution:
    def maximumEvenSplit(self, finalSum: int) -> list[int]:
        if finalSum % 2:
            return []

        to_add = 2
        added = []

        while finalSum >= to_add:
            finalSum -= to_add
            added.append(to_add)
            to_add += 2

        added[-1] += finalSum

        return added
