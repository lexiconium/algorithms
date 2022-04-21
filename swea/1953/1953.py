import os
import sys

sys.stdin = open(
    os.path.join("/", *__file__.split("/")[:-1], "sample_input.txt"), "r"
)

import heapq

DR = [-1, 0, 1, 0]
DC = [0, 1, 0, -1]

STRUCT = {
    0: [],
    1: [0, 1, 2, 3],
    2: [0, 2],
    3: [1, 3],
    4: [0, 1],
    5: [1, 2],
    6: [2, 3],
    7: [3, 0],
}


def is_valid(tunnel: list[list[int]], r: int, c: int):
    return 0 <= r < len(tunnel) and 0 <= c < len(tunnel[0])


def is_connected(d: int, struct_id: int):
    return (d + 2) % 4 in STRUCT[struct_id]


def bfs(tunnel: list[list[int]], r: int, c: int, l: int):
    visited = {(r, c)}

    pq = [(1, r, c)]
    while pq:
        t, r, c = heapq.heappop(pq)
        if t == l:
            return len(visited)

        for d in STRUCT[tunnel[r][c]]:
            _r, _c = r + DR[d], c + DC[d]
            if not is_valid(tunnel, _r, _c):
                continue
            if not is_connected(d, tunnel[_r][_c]):
                continue
            if (_r, _c) in visited:
                continue

            heapq.heappush(pq, (t + 1, _r, _c))
            visited.add((_r, _c))

    return len(visited)


for t in range(1, int(input()) + 1):
    m, n, r, c, l = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(m)]
    print(f"#{t} {bfs(tunnel, r, c, l)}")
