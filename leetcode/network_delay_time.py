# https://leetcode.com/problems/network-delay-time/description/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, t in times:
            graph[u].append((v, t))

        pq = [(0, k)]
        visited = 1 << (k - 1)
        visited_all = (1 << n) - 1

        min_time = 0

        while pq:
            t, u = heapq.heappop(pq)

            visited |= 1 << (u - 1)
            min_time = max(min_time, t)

            if visited == visited_all:
                return min_time

            for v, dt in graph[u]:
                if (1 << (v - 1)) & visited:
                    continue

                heapq.heappush(pq, (t + dt, v))

        return -1
