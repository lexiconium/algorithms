import heapq


def solution(maze):
    rp = bp = rd = bd = None

    for r, row in enumerate(maze):
        for c, v in enumerate(row):
            if v == 1:
                rp = (r, c)
            elif v == 2:
                bp = (r, c)
            elif v == 3:
                rd = (r, c)
            elif v == 4:
                bd = (r, c)

    num_rows, num_cols = len(maze), len(maze[0])

    def in_bound(r, c):
        return 0 <= r < num_rows and 0 <= c < num_cols

    def next_points(p, d, visited):
        if p == d:
            yield d

        r, c = p

        for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            if not in_bound(nr := r + dr, nc := c + dc):
                continue
            if maze[nr][nc] == 5:
                continue
            if (1 << (nr * num_cols + nc)) & visited:
                continue

            yield nr, nc

    pq = [(0, rp, bp, 1 << (rp[0] * num_cols + rp[1]), 1 << (bp[0] * num_cols + bp[1]))]

    while pq:
        num_turns, rp, bp, r_visited, b_visited = heapq.heappop(pq)

        if rp == rd and bp == bd:
            return num_turns

        for rnp in next_points(rp, rd, r_visited):
            for bnp in next_points(bp, bd, b_visited):
                if rnp == bnp or rnp == bp and bnp == rp:
                    continue

                heapq.heappush(
                    pq,
                    (
                        num_turns + 1,
                        rnp,
                        bnp,
                        r_visited | (1 << (rnp[0] * num_cols + rnp[1])),
                        b_visited | (1 << (bnp[0] * num_cols + bnp[1])),
                    ),
                )

    return 0
