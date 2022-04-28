import os
import sys

sys.stdin = open(
    os.path.join("/", *__file__.split("/")[:-1], "sample_input.txt"), "r"
)

# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV597vbqAH0DFAVl


DR = [-1, 1, 0, 0]
DC = [0, 0, -1, 1]


class Cluster:
    def __init__(self, r: int, c: int, n: int, d: int):
        self.loc = (r, c)
        self.n = n
        self.d = d - 1

    def __iadd__(self, other):
        self.n += other.n
        return self

    def __repr__(self):
        return str(self.n)


def is_boundary(r: int, c: int):
    return r == 0 or r == m - 1 or c == 0 or c == m - 1


def step():
    cluster_map = [[0 for _ in range(m)] for _ in range(m)]
    for _id in sorted(
        list(clusters.keys()), key=lambda _id: clusters[_id].n, reverse=True
    ):
        cluster = clusters[_id]

        r, c = cluster.loc
        _r, _c = r + DR[cluster.d], c + DC[cluster.d]

        if is_boundary(_r, _c):
            cluster.n //= 2
            cluster.d ^= 1

        if cluster_map[_r][_c]:
            clusters[cluster_map[_r][_c]] += cluster
            clusters.pop(_id)
            continue

        if not cluster.n:
            clusters.pop(_id)
            continue

        cluster.loc = (_r, _c)
        cluster_map[_r][_c] = _id


for t in range(1, int(input()) + 1):
    m, n, k = map(int, input().split())
    clusters = {
        _id: Cluster(*map(int, input().split())) for _id in range(1, k + 1)
    }
    for _ in range(n):
        step()

    print(f"#{t} {sum(cluster.n for cluster in clusters.values())}")
