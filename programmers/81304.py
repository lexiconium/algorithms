import heapq
from collections import defaultdict


def build_graph(relation):
    graph = defaultdict(lambda: defaultdict(list))

    for u, v, e in relation:
        graph[u][v].append(e)
        graph[v][u].append(-e)

    return graph


def solution(n, start, end, roads, traps):
    graph = build_graph(roads)
    traps = {n: i for i, n in enumerate(traps)}

    def is_active(trap_status, node):
        if node not in traps:
            return False
        return bool(trap_status & (1 << traps[node]))

    def update_status(trap_status, node):
        if node in traps:
            trap_status ^= (1 << traps[node])
        return trap_status

    pq = [(0, start, 0)]

    reaching_times = {m: defaultdict(lambda: float("inf")) for m in range(1, n + 1)}
    reaching_times[start][0] = 0

    while pq:
        time, node, trap_status = heapq.heappop(pq)

        if node == end:
            return time

        for adj, dts in graph[node].items():
            sign = 1 if is_active(trap_status, node) == is_active(trap_status, adj) else -1

            for dt in dts:
                if (dt := sign * dt) < 0:
                    continue
                if reaching_times[adj][trap_status] < (nt := time + dt):
                    continue

                heapq.heappush(pq, (nt, adj, update_status(trap_status, adj)))
                reaching_times[adj][trap_status] = nt
