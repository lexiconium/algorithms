# https://leetcode.com/problems/array-partition-i/

# time complexity: O(nlog(n))

class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        return sum(sorted(nums)[::2])