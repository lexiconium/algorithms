# https://programmers.co.kr/learn/courses/30/lessons/86971

from collections import defaultdict, deque


def make_graph(wires):
    graph = defaultdict(list)
    for u, v in wires:
        graph[u].append(v)
        graph[v].append(u)

    return graph


def count_nodes_one_of(graph, *, exclude):
    u, v = exclude

    q = deque([u])
    visited = {u}

    cnt = 1
    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if neighbor in visited:
                continue
            if neighbor == v:
                continue

            q.append(neighbor)
            visited.add(neighbor)
            cnt += 1

    return cnt


def solution(n, wires):
    graph = make_graph(wires)

    min_diff = n
    for exclude_idx in range(n - 1):
        min_diff = min(
            min_diff,
            abs(n - 2 * count_nodes_one_of(graph, exclude=wires[exclude_idx])),
        )

    return min_diff
