# https://leetcode.com/problems/path-sum-iii/description/


from collections import defaultdict
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        path_sum_counter = defaultdict(int)
        path_sum_counter[0] += 1

        def dfs(node: Optional[TreeNode], path_sum: int = 0) -> int:
            if node is None:
                return 0

            path_sum += node.val
            cnt = path_sum_counter[path_sum - targetSum]

            path_sum_counter[path_sum] += 1
            cnt += dfs(node.left, path_sum) + dfs(node.right, path_sum)
            path_sum_counter[path_sum] -= 1

            return cnt

        return dfs(root)
