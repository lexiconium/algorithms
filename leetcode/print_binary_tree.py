# https://leetcode.com/problems/print-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def get_depth(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            return max(get_depth(node.left), get_depth(node.right)) + 1

        height = get_depth(root)
        width = 2 ** height - 1

        tree = [["" for _ in range(width)] for _ in range(height)]

        def draw(
                node: Optional[TreeNode], depth: int, lbound: int, rbound: int
        ) -> None:
            if node is None:
                return

            tree[depth][i := (lbound + rbound) // 2] = str(node.val)

            draw(node.left, depth + 1, lbound, i)
            draw(node.right, depth + 1, i, rbound)

        draw(root, 0, 0, width)

        return tree
