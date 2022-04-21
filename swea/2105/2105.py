import os
import sys

sys.stdin = open(
    os.path.join("/", *__file__.split("/")[:-1], "sample_input.txt"), "r"
)

# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5VwAr6APYDFAWu

DR = [-1, 1, 1, -1]
DC = [1, 1, -1, -1]


def are_desserts_unique(r: int, c: int, ll2ur_diag: int, ul2lr_diag: int):
    desserts = 1 << m[r][c]
    route = (
        [0 for _ in range(ll2ur_diag)]
        + [1 for _ in range(ul2lr_diag)]
        + [2 for _ in range(ll2ur_diag)]
        + [3 for _ in range(ul2lr_diag - 1)]
    )
    for d in route:
        r, c = r + DR[d], c + DC[d]
        dessert = 1 << m[r][c]
        if desserts & dessert:
            return False
        desserts |= dessert

    return True


def max_num_desserts(r: int, c: int):
    num_desserts = -1
    for ll2ur_diag in range(1, min(r + 1, n - c)):
        for ul2lr_diag in range(1, min(n - r, n - (c + ll2ur_diag))):
            if are_desserts_unique(r, c, ll2ur_diag, ul2lr_diag):
                num_desserts = max(num_desserts, 2 * (ll2ur_diag + ul2lr_diag))

    return num_desserts


for t in range(1, int(input()) + 1):
    n = int(input())
    m = [list(map(int, input().split())) for _ in range(n)]
    print(
        f"#{t} {max(max_num_desserts(r, c) for r in range(n) for c in range(n))}"
    )
