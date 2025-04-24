# https://leetcode.com/problems/binary-search-tree-iterator/description/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode | None) -> None:
        self.stack = []
        self._append_lefts(root)

    def next(self) -> int:
        self._append_lefts((node := self.stack.pop()).right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

    def _append_lefts(self, node: TreeNode | None) -> None:
        while node:
            self.stack.append(node)
            node = node.left


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
