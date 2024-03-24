from collections import defaultdict, deque


def solution(edges):
    # make graph
    # out only & num_outs >= 2 vertex -> unique
    graph = defaultdict(lambda: set())
    out_in_diffs = defaultdict(int)

    for u, v in edges:
        graph[u].add(v)
        out_in_diffs[u] += 1
        out_in_diffs[v] -= 1

    generated_vertex = None

    for u, vs in graph.items():
        if len(vs) != out_in_diffs[u]:
            continue
        if len(vs) < 2:
            continue

        generated_vertex = u
        break

    cnts = [0, 0, 0]

    def identify_index(v):
        q = deque([v])

        while q:
            node = q.popleft()

            if (n := len(graph[node])) == 0:
                return 1
            if n > 1:
                return 2

            for next_node in graph[node]:
                if next_node == v:
                    return 0

                q.append(next_node)

    # identify shapes
    for v in graph[generated_vertex]:
        cnts[identify_index(v)] += 1

    return [generated_vertex, *cnts]
