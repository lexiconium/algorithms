# https://leetcode.com/problems/add-one-row-to-tree/submissions/940524673/

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: TreeNode | None, val: int, depth: int) -> TreeNode | None:
        q = deque([(dummy := TreeNode(left=root), 0)])

        while q:
            node, d = q.popleft()

            if node is None:
                continue

            if d == depth - 1:
                node.left, node.right = (
                    TreeNode(val, left=node.left),
                    TreeNode(val, right=node.right),
                )

                continue

            q.append((node.left, d + 1))
            q.append((node.right, d + 1))

        return dummy.left
