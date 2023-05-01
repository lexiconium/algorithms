# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def get_height(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            return max(get_height(node.left), get_height(node.right)) + 1

        height = get_height(root)
        width = 2 * height - 1

        vertical_ordered = [[] for _ in range(2 * height - 1)]

        def fill(node: Optional[TreeNode], r: int, c: int) -> None:
            if node is None:
                return

            vertical_ordered[c].append((r, node.val))

            fill(node.left, r + 1, c - 1)
            fill(node.right, r + 1, c + 1)

        fill(root, 0, width // 2)

        return [[v[1] for v in sorted(vs)] for vs in vertical_ordered if vs]
