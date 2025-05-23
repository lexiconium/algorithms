# https://leetcode.com/problems/flip-equivalent-binary-trees/description/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipEquiv(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        if root1.val == root2.val:
            return (
                self.flipEquiv(root1.left, root2.left)
                and self.flipEquiv(root1.right, root2.right)
                or self.flipEquiv(root1.left, root2.right)
                and self.flipEquiv(root1.right, root2.left)
            )
        return False
