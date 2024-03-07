# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance


class Solution:
    def findTheCity(
        self, n: int, edges: list[list[int]], distanceThreshold: int
    ) -> int:
        dists_from_nodes = [[float("inf")] * n for _ in range(n)]

        for i in range(n):
            dists_from_nodes[i][i] = 0

        for i, j, w in edges:
            dists_from_nodes[i][j] = dists_from_nodes[j][i] = w

        for k in range(n):
            for i in range(n - 1):
                if i == k:
                    continue

                for j in range(i + 1, n):
                    if j == k:
                        continue

                    dists_from_nodes[i][j] = min(
                        dists_from_nodes[i][k] + dists_from_nodes[k][j],
                        dists_from_nodes[i][j],
                    )
                    dists_from_nodes[j][i] = dists_from_nodes[i][j]

        num_neighbors = [
            (sum(dist <= distanceThreshold for dist in dists), -i)
            for i, dists in enumerate(dists_from_nodes)
        ]

        return -sorted(num_neighbors)[0][1]
