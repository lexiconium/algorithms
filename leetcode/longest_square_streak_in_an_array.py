# https://leetcode.com/problems/longest-square-streak-in-an-array/description/


class Solution:
    def longestSquareStreak(self, nums: list[int]) -> int:
        cache = {}
        longest = 1

        for n in sorted(nums, reverse=True):
            if (nsq := n**2) in cache:
                cache[n] = cache[nsq] + 1
            else:
                cache[n] = 1

            longest = max(cache[n], longest)

        return longest if longest > 1 else -1
