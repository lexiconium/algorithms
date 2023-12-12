# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: TreeNode | None) -> int:
        def dfs(node: TreeNode | None) -> tuple[int, int, int]:
            if node is None:
                return 0, 0, 0

            _, lr, lmax = dfs(node.left)
            rl, _, rmax = dfs(node.right)

            lr += (node.left is not None)
            rl += (node.right is not None)

            return lr, rl, max(lr, rl, lmax, rmax)

        _, _, longest = dfs(root)

        return longest
