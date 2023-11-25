# https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/description/
# TODO

from collections import defaultdict, deque


class Solution:
    def minCost(self, max_time: int, edges: list[list[int]], passing_fees: list[int]) -> int:
        graph = defaultdict(lambda: defaultdict(lambda: float("inf")))
        for u, v, t in edges:
            graph[u][v] = min(t, graph[u][v])
            graph[v][u] = graph[u][v]

        visited = [(float("inf"), float("inf")) for _ in passing_fees]
        num_nodes = len(passing_fees)

        q = deque([(0, 0, passing_fees[0])])
        while q:
            node, time, cost = q.popleft()

            if time > max_time:
                continue

            if cost < visited[node][0]:
                visited[node] = (cost, time)
            elif time >= visited[node][1]:
                continue

            for adj_node, dt in graph[node].items():
                q.append((adj_node, time + dt, cost + passing_fees[adj_node]))

        return -1 if visited[num_nodes - 1][0] == float("inf") else visited[num_nodes - 1][0]
