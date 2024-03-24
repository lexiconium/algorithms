from collections import deque


def solution(n, m, x, y, queries):
    def next_points(r, c, d, dist):
        dr, dc = ((0, 1), (0, -1), (1, 0), (-1, 0))[d]

        if r == 0 and dr == 1:
            for nr in range(r, min(r + dist + 1, n)):
                yield nr, c
        elif r == n - 1 and dr == -1:
            for nr in range(max(r - dist, 0), r + 1):
                yield nr, c
        elif c == 0 and dc == 1:
            for nc in range(c, min(c + dist + 1, m)):
                yield r, nc
        elif c == m - 1 and dc == -1:
            for nc in range(max(c - dist, 0), c + 1):
                yield r, nc
        elif 0 <= (nr := r + dist * dr) < n and 0 <= (nc := c + dist * dc) < m:
            yield nr, nc

    q = deque([(x, y, -1)])
    start_points = set()

    while q:
        r, c, query_index = q.popleft()

        if abs(query_index) > len(queries):
            start_points.add((r, c))
            continue

        for nr, nc in next_points(r, c, *queries[query_index]):
            q.append((nr, nc, query_index - 1))

    return len(start_points)
