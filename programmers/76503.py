import sys
from collections import defaultdict

sys.setrecursionlimit(300000)


def solution(a, edges):
    if sum(a):
        return -1

    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def dfs(node=0, parent=-1):
        if node and len(graph[node]) == 1:
            return a[node], 0

        value = a[node]
        num_ops = 0

        for child in graph[node]:
            if child == parent:
                continue

            child_value, num_child_ops = dfs(child, node)

            value += child_value
            num_ops += abs(child_value) + num_child_ops

        return value, num_ops

    return dfs(0)[1]
