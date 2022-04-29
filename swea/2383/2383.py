import os
import sys

sys.stdin = open(
    os.path.join("/", *__file__.split("/")[:-1], "sample_input.txt"), "r"
)

# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5-BEE6AK0DFAVl


from collections import deque


def takes(selected: int):
    dists_to_0, dists_to_1 = [], []
    for idx in range(len(people))[::-1]:
        uses0 = selected & 1
        if uses0:
            dists_to_0.append(dists[idx][0])
        else:
            dists_to_1.append(dists[idx][1])
        selected >>= 1

    dists_to_0, dists_to_1 = sorted(dists_to_0), sorted(dists_to_1)

    q0 = deque([], maxlen=3)
    for dist_to_0 in dists_to_0:
        if len(q0) == 3:
            q0.append(max(dist_to_0 + 1, q0[0]) + stairs[0][2])
        else:
            q0.append(dist_to_0 + 1 + stairs[0][2])

    q1 = deque([], maxlen=3)
    for dist_to_1 in dists_to_1:
        if len(q1) == 3:
            q1.append(max(dist_to_1 + 1, q1[0]) + stairs[1][2])
        else:
            q1.append(dist_to_1 + 1 + stairs[1][2])

    return max(max(q0, default=0), max(q1, default=0))


def select(idx: int = 0, selected: int = 0):
    if idx == len(people):
        return takes(selected)
    return min(
        select(idx + 1, selected), select(idx + 1, selected | (1 << idx))
    )


for t in range(1, int(input()) + 1):
    n = int(input())
    people = []
    stairs = []
    for r in range(n):
        for c, v in enumerate(list(map(int, input().split()))):
            if not v:
                continue
            if v == 1:
                people.append((r, c))
            else:
                stairs.append((r, c, v))

    dists = [
        (
            abs(r - stairs[0][0]) + abs(c - stairs[0][1]),
            abs(r - stairs[1][0]) + abs(c - stairs[1][1]),
        )
        for r, c in people
    ]

    print(f"#{t} {select()}")
