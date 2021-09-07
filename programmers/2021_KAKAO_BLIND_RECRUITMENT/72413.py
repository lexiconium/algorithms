# https://programmers.co.kr/learn/courses/30/lessons/72413

from collections import defaultdict
import heapq

def solution(n, s, a, b, fares):
    graph = defaultdict(list)
    for u, v, cost in fares:
        graph[u].append((v, cost))
        graph[v].append((u, cost))
    
    def dijkstra(start):
        dist = [float('inf') for _ in range(n + 1)]
        q = [(0, start)]
        while q:
            cost, prev = heapq.heappop(q)
            if dist[prev] == float('inf'):
                dist[prev] = cost
                for v, _cost in graph[prev]:
                    heapq.heappush(q, (cost + _cost, v))
        return dist
    
    min_costs = [[]] + [dijkstra(start) for start in range(1, n + 1)]
    tot_cost = float('inf')
    for split in range(1, n + 1):
        tot_cost = min(min_costs[s][split] + min_costs[a][split] + min_costs[b][split], tot_cost)
    
    return tot_cost
