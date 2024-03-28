# https://leetcode.com/problems/house-robber-iii/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode | None) -> int:
        def dfs(node: TreeNode | None) -> tuple[int, int]:
            if node is None:
                return (0, 0)

            left, right = dfs(node.left), dfs(node.right)

            return (node.val + left[1] + right[1], max(left) + max(right))

        return max(dfs(root))
