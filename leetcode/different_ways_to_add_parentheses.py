# https://leetcode.com/problems/different-ways-to-add-parentheses/

import re


class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        nums = list(map(int, re.findall("\d+", expression)))
        ops = re.findall("\+|\-|\*", expression)

        def apply(left: int, right: int, op: str) -> int:
            if op == "+":
                return left + right
            if op == "-":
                return left - right
            return left * right

        dp = [[[] for _ in nums] for _ in nums]

        for i in reversed(range(len(nums))):
            dp[i][i] = [nums[i]]

            for j in range(i + 1, len(nums)):
                for k in range(i, j):
                    dp[i][j].extend([
                        apply(left, right, ops[k])
                        for left in dp[i][k] for right in dp[k + 1][j]
                    ])

        return dp[0][-1]

    # simple recurrent
    def diffWaysToCompute(self, expression: str) -> list[int]:
        if expression.isnumeric():
            return [int(expression)]

        def apply(l: int, r: int, op: str) -> int:
            if op == "+":
                return l + r
            if op == "-":
                return l - r
            return l * r

        possibles = []

        for i, c in enumerate(expression):
            if c.isnumeric():
                continue

            left = self.diffWaysToCompute(expression[:i])
            right = self.diffWaysToCompute(expression[i + 1:])

            possibles.extend([apply(l, r, c) for l in left for r in right])

        return possibles
