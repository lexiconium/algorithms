import os
import sys

sys.stdin = open(
    os.path.join("/", *__file__.split("/")[:-1], "sample_input.txt"), "r"
)

# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V1SYKAaUDFAWu


def is_valid(injected: set[int]):
    transformed = {}
    for injection in injected:
        t, idx = divmod(injection, d)
        transformed[idx] = t

    for vertical in film_t:
        max_consequtives = 1
        begin = 0
        begin_t = transformed[0] if 0 in transformed else vertical[0]
        for idx in range(1, d):
            _t = transformed[idx] if idx in transformed else vertical[idx]
            if begin_t != _t:
                begin = idx
                begin_t = _t
            else:
                max_consequtives = max(max_consequtives, idx - begin + 1)

        if max_consequtives < k:
            return False
    return True


def dfs(idx: int = 0, injected: set[int] = set()):
    if idx == d:
        return len(injected) if is_valid(injected) else d

    return min(
        dfs(idx + 1, injected),
        dfs(idx + 1, injected | {idx}),
        dfs(idx + 1, injected | {d + idx}),
    )


for t in range(1, int(input()) + 1):
    d, w, k = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(d)]
    film_t = list(zip(*film))
    print(f"#{t} {dfs()}")
