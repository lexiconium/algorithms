# https://leetcode.com/problems/reachable-nodes-with-restrictions/description/


from collections import defaultdict, deque


class Solution:
    def reachableNodes(
        self, n: int, edges: list[list[int]], restricted: list[int]
    ) -> int:
        restricted = set(restricted)

        graph = defaultdict(list)
        for u, v in edges:
            if u in restricted or v in restricted:
                continue

            graph[u].append(v)
            graph[v].append(u)

        q = deque([0])
        visited = {0}

        while q:
            node = q.popleft()
            visited.add(node)

            for adj in graph[node]:
                if adj in visited:
                    continue

                q.append(adj)

        return len(visited)
