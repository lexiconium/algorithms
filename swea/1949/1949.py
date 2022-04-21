import os
import sys

sys.stdin = open(
    os.path.join("/", *__file__.split("/")[:-1], "sample_input.txt"), "r"
)

# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PoOKKAPIDFAUq

from collections import deque
from copy import copy

DR = [-1, 0, 1, 0]
DC = [0, 1, 0, -1]


def is_valid(r: int, c: int):
    return 0 <= r < len(m) and 0 <= c < len(m[0])


def bfs(r: int, c: int, k: int):
    visited = set()
    q = deque([(1, r, c, m[r][c], True, visited)])
    max_dist = 1

    while q:
        dist, r, c, h, can_carve, visited = q.popleft()
        max_dist = max(max_dist, dist)
        visited.add((r, c))

        for d in range(4):
            _r, _c = r + DR[d], c + DC[d]
            if not is_valid(_r, _c):
                continue
            if (_r, _c) in visited:
                continue

            if m[_r][_c] < h:
                q.append(
                    (dist + 1, _r, _c, m[_r][_c], can_carve, copy(visited))
                )
            elif can_carve and m[_r][_c] - k < h:
                q.append((dist + 1, _r, _c, h - 1, False, copy(visited)))

    return max_dist


def max_height_points():
    max_height = max(max(row) for row in m)
    return (
        (r, c)
        for r, row in enumerate(m)
        for c, h in enumerate(row)
        if h == max_height
    )


for t in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    m = [list(map(int, input().split())) for _ in range(n)]
    print(f"#{t} {max(bfs(r, c, k) for r, c in max_height_points())}")
