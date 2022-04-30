# https://www.acmicpc.net/problem/17142

from collections import deque
from itertools import combinations


DR = [-1, 0, 1, 0]
DC = [0, 1, 0, -1]


def is_valid(r: int, c: int):
    return 0 <= r < m and 0 <= c < m and lab_map[r][c] != 1


def bfs():
    min_takes = float("inf")
    for _virus_locs in combinations(virus_locs, n):
        q = deque([(0, *virus_loc) for virus_loc in _virus_locs])
        visited = {virus_loc for virus_loc in _virus_locs}
        _max = 0
        while q:
            t, r, c = q.popleft()
            if (r, c) not in virus_locs:
                _max = max(_max, t)
            for d in range(4):
                _r, _c = r + DR[d], c + DC[d]
                if not is_valid(_r, _c) or (_r, _c) in visited:
                    continue
                q.append((t + 1, _r, _c))
                visited.add((_r, _c))

        if len(visited) - len(virus_locs) != empties:
            continue

        min_takes = min(min_takes, _max)
    return -1 if min_takes == float("inf") else min_takes


m, n = map(int, input().split())
lab_map = [list(map(int, input().split())) for _ in range(m)]
virus_locs = set()
empties = 0
for r, row in enumerate(lab_map):
    for c, v in enumerate(row):
        if not v:
            empties += 1
        elif v == 2:
            virus_locs.add((r, c))

print(bfs())
