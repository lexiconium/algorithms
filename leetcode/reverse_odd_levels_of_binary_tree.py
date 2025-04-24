# https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root: TreeNode | None) -> TreeNode | None:
        def exchange_values(
            left: TreeNode | None, right: TreeNode | None, level: int
        ) -> None:
            if left is None:
                return

            if level % 2:
                left.val, right.val = right.val, left.val

            exchange_values(left.left, right.right, level + 1)
            exchange_values(left.right, right.left, level + 1)

        exchange_values(root.left, root.right, 1)

        return root
