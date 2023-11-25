# https://leetcode.com/problems/frog-jump-ii/description/


class Solution:
    def maxJump(self, stones: list[int]) -> int:
        if len(stones) == 2:
            return stones[1] - stones[0]
        return max(stones[i + 2] - stones[i] for i in range(len(stones) - 2))
