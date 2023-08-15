# https://leetcode.com/problems/largest-color-value-in-a-directed-graph/submissions/

from collections import defaultdict, deque


class Solution:
    def largestPathValue(self, colors: str, edges: list[list[int]]) -> int:
        graph = defaultdict(
            lambda: {"child": [], "color_info": defaultdict(int), "num_directed": 0}
        )

        for u, v in edges:
            graph[u]["child"].append(v)
            graph[v]["num_directed"] += 1

        for node, c in enumerate(colors):
            graph[node]["color_info"][c] += 1

        q = deque([node for node, info in graph.items() if info["num_directed"] == 0])
        max_cnt = 0
        num_visited = 0

        while q:
            u = q.popleft()

            max_cnt = max(max(graph[u]["color_info"].values()), max_cnt)

            for v in graph[u]["child"]:
                for c, cnt in graph[u]["color_info"].items():
                    graph[v]["color_info"][c] = max(
                        cnt + (colors[v] == c), graph[v]["color_info"][c]
                    )

                graph[v]["num_directed"] -= 1
                if graph[v]["num_directed"] < 0:
                    return -1
                if graph[v]["num_directed"] == 0:
                    q.append(v)

            num_visited += 1

        return max_cnt if num_visited == len(graph) else -1
