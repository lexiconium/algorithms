# https://school.programmers.co.kr/learn/courses/30/lessons/92343

from collections import defaultdict, deque
from copy import deepcopy


def make_graph(edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    return graph


def get_maximum_sheep(info, graph):
    max_sheep = 0

    init_visited = [[1, 0]] + [None] * (len(info) - 1)
    q = deque([(0, init_visited)])
    while q:
        node, visited = q.popleft()
        max_sheep = max(max_sheep, visited[node][0])

        for adjacent in graph[node]:
            if visited[adjacent] == visited[node]:
                continue

            _visited = deepcopy(visited)
            status = _visited[node][:]

            if _visited[adjacent] is None:
                status[info[adjacent]] += 1

            if status[0] <= status[1]:
                continue

            _visited[adjacent] = status
            q.append((adjacent, _visited))

    return max_sheep


def solution(info, edges):
    graph = make_graph(edges)
    return get_maximum_sheep(info, graph)
