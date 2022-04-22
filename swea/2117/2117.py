import os
import sys

sys.stdin = open(
    os.path.join("/", *__file__.split("/")[:-1], "sample_input.txt"), "r"
)

# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V61LqAf8DFAWu


def is_valid(r: int, c: int):
    return 0 <= r < n and 0 <= c < n


def max_dist(r: int, c: int):
    _dist = dist = 0
    num_households = []
    _num_households = 0
    while 1 + 2 * dist * (dist + 1) <= pay * tot_households:
        for dr in range(-dist, dist + 1):
            for dc in range(-dist, dist + 1):
                if abs(dr) + abs(dc) != dist:
                    continue
                _r, _c = r + dr, c + dc
                if not is_valid(_r, _c):
                    continue

                _num_households += m[_r][_c]

        num_households.append(_num_households)

        if 1 + 2 * dist * (dist + 1) <= pay * _num_households:
            _dist = dist

        dist += 1

    return num_households[_dist]


def max_coverage():
    return max(max_dist(r, c) for r in range(n) for c in range(n))


for t in range(1, int(input()) + 1):
    n, pay = map(int, input().split())
    m = [list(map(int, input().split())) for _ in range(n)]
    tot_households = sum(sum(row) for row in m)
    print(f"#{t} {max_coverage()}")
