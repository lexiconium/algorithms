import os
import sys

sys.stdin = open(
    os.path.join("/", *__file__.split("/")[:-1], "sample_input.txt"), "r"
)

# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V1SYKAaUDFAWu

from itertools import combinations


def is_valid(injected: list[int]):
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


def min_num_injections():
    for num_injection in range(d):
        for injected in map(list, combinations(range(d), r=num_injection)):
            for num_b in range(num_injection + 1):
                for b_idxs in combinations(range(num_injection), r=num_b):
                    for b_idx in b_idxs:
                        injected[b_idx] += d

                    if is_valid(injected):
                        return num_injection

                    for b_idx in b_idxs:
                        injected[b_idx] -= d
    return d


for t in range(1, int(input()) + 1):
    d, w, k = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(d)]
    film_t = list(zip(*film))
    print(f"#{t} {min_num_injections()}")
