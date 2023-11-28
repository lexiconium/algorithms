# https://leetcode.com/problems/egg-drop-with-2-eggs-and-n-floors/
import math


class Solution:
    def twoEggDrop(self, n: int) -> int:
        return math.ceil((-1 + (1 + 8 * n) ** 0.5) / 2)
