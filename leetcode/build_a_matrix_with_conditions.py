# https://leetcode.com/problems/build-a-matrix-with-conditions/description/

from collections import defaultdict, deque


class Solution:
    def buildMatrix(
        self, k: int, rowConditions: list[list[int]], colConditions: list[list[int]]
    ) -> list[list[int]]:
        def topological_sorted(conditions: list[tuple[int, int]]) -> list[int]:
            graph = defaultdict(list)
            counter = defaultdict(int)

            for high, low in conditions:
                graph[high].append(low)
                counter[low] += 1

            q = deque([node for node in range(1, k + 1) if counter[node] == 0])
            sorted_nodes = []

            while q:
                node = q.popleft()
                sorted_nodes.append(node)

                for children in graph[node]:
                    counter[children] -= 1

                    if counter[children] == 0:
                        q.append(children)

            if len(sorted_nodes) < k:
                return []

            return sorted_nodes

        if not (row_sorted := topological_sorted(rowConditions)):
            return []

        if not (col_sorted := topological_sorted(colConditions)):
            return []

        mat = [[0 for _ in range(k)] for _ in range(k)]
        col_sorted_indices = {v: i for i, v in enumerate(col_sorted)}

        for r, v in enumerate(row_sorted):
            mat[r][col_sorted_indices[v]] = v

        return mat
