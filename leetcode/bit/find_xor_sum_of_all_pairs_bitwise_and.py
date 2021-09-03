# https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and/

# time complexity: O(n)

class Solution:
    def getXORSum(self, arr1: list[int], arr2: list[int]) -> int:
        a = b = 0
        for n in arr1:
            a ^= n
        for n in arr2:
            b ^= n
        return a & b