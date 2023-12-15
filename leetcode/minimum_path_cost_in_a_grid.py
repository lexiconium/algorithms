# https://leetcode.com/problems/minimum-path-cost-in-a-grid/description/

from copy import deepcopy


class Solution:
    def minPathCost(self, grid: list[list[int]], moveCost: list[list[int]]) -> int:
        num_rows, num_columns = len(grid), len(grid[0])

        min_costs = deepcopy(grid)

        for r in reversed(range(num_rows - 1)):
            for c in range(num_columns):
                min_costs[r][c] += min(
                    min_costs[r + 1][nc] + moveCost[v := grid[r][c]][nc]
                    for nc in range(num_columns)
                )

        return min(min_costs[0])
