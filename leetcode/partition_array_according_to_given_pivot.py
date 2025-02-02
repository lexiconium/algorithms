# https://leetcode.com/problems/partition-array-according-to-given-pivot/


class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        lt, eq, gt = [], [], []

        for n in nums:
            if n < pivot:
                lt.append(n)
            elif n == pivot:
                eq.append(n)
            else:
                gt.append(n)

        return lt + eq + gt
