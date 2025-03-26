# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/


from collections import defaultdict, deque


class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        graph = defaultdict(list)
        for a, b, dist in roads:
            graph[a].append((b, dist))
            graph[b].append((a, dist))

        min_dist = float("inf")

        q = deque([1])
        visited = {1}

        while q:
            node = q.popleft()

            for adj, dist in graph[node]:
                min_dist = min(dist, min_dist)

                if adj in visited:
                    continue

                q.append(adj)
                visited.add(adj)

        return min_dist
