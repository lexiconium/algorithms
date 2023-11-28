# https://leetcode.com/problems/all-possible-full-binary-trees/description/

from functools import cache


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @cache
    def allPossibleFBT(self, n: int) -> list[TreeNode | None]:
        if n == 1:
            return [TreeNode()]

        return [
            TreeNode(left=left, right=right)
            for m in range(1, n - 1, 2)
            for left in self.allPossibleFBT(m)
            for right in self.allPossibleFBT(n - m - 1)
        ]
