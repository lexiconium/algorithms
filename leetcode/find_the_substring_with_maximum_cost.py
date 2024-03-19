# https://leetcode.com/problems/find-the-substring-with-maximum-cost/description/


class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: list[int]) -> int:
        costs = {c: vals[i] for i, c in enumerate(chars)}

        cur = max_cost = 0

        for c in s:
            cur = max(cur + costs.get(c, ord(c) - ord("a") + 1), 0)
            max_cost = max(cur, max_cost)

        return max_cost
