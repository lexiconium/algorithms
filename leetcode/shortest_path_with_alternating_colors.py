# https://leetcode.com/problems/shortest-path-with-alternating-colors/description/


from collections import deque, defaultdict


class Solution:
    def shortestAlternatingPaths(
        self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]
    ) -> list[int]:
        graph = defaultdict(lambda: [[], []])

        for u, v in redEdges:
            graph[u][0].append(v)

        for u, v in blueEdges:
            graph[u][1].append(v)

        q = deque([(0, 0, 0), (0, 1, 0)])

        distances = [[float("inf"), float("inf")] for _ in range(n)]
        distances[0] = [0, 0]

        while q:
            node, prev_color, dist = q.popleft()

            next_color = prev_color ^ 1

            for next_node in graph[node][next_color]:
                if distances[next_node][next_color] < dist + 1:
                    continue

                distances[next_node][next_color] = dist + 1
                q.append((next_node, next_color, dist + 1))

        def inf_to_m1(num) -> int:
            return -1 if num == float("inf") else num

        return [inf_to_m1(min(r_dist, b_dist)) for r_dist, b_dist in distances]
