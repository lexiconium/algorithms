from collections import defaultdict, deque


def solution(n, roads, sources, destination):
    graph = defaultdict(list)

    for u, v in roads:
        graph[u].append(v)
        graph[v].append(u)

    min_dists = {node: float("inf") for node in range(1, n + 1)}
    min_dists[destination] = 0

    q = deque([(destination, 0)])

    while q:
        node, dist = q.popleft()

        for adj in graph[node]:
            if min_dists[adj] <= dist + 1:
                continue

            min_dists[adj] = dist + 1
            q.append((adj, dist + 1))

    return [
        -1 if min_dists[source] == float("inf") else min_dists[source]
        for source in sources
    ]
