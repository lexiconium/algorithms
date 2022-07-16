# https://school.programmers.co.kr/learn/courses/30/lessons/92343

from collections import defaultdict


def make_graph(edges):
    graph = defaultdict(set)
    for u, v in edges:
        graph[u].add(v)

    return graph


def solution(info, edges):
    graph = make_graph(edges)

    def dfs(node, sheep, wolf, children):
        sheep += info[node] == 0
        wolf += info[node] == 1

        if not sheep > wolf:
            return -1

        max_sheep = sheep
        for child in children:
            max_sheep = max(
                max_sheep,
                dfs(child, sheep, wolf, (children - {child}) | graph[child]),
            )

        return max_sheep

    return dfs(0, 0, 0, graph[0])
