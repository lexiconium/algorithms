# https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/

from functools import cache


class Solution:
    def mctFromLeafValues(self, arr: list[int]) -> int:
        @cache
        def dfs(begin: int, end: int) -> tuple[int, int]:
            if end - begin == 1:
                return arr[begin], 0

            largest_leaf, min_sum = 0, float("inf")

            for i in range(1, end - begin):
                left_largest_leaf, left_sum = dfs(begin, begin + i)
                right_largest_leaf, right_sum = dfs(begin + i, end)

                if (cand_sum := left_sum + left_largest_leaf * right_largest_leaf + right_sum) < min_sum:
                    largest_leaf = max(left_largest_leaf, right_largest_leaf)
                    min_sum = cand_sum

            return largest_leaf, min_sum

        return dfs(0, len(arr))[1]

    # https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/solutions/339959/one-pass-o-n-time-and-space/
    def mctFromLeafValues(self, arr: list[int]) -> int:
        min_sum = 0

        stack = [float("inf")]

        for n in arr:
            while stack[-1] <= n:
                m = stack.pop()
                min_sum += m * min(stack[-1], n)

            stack.append(n)

        while len(stack) > 2:
            min_sum += stack.pop() * stack[-1]

        return min_sum
