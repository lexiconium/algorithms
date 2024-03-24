import math


def solution(r1, r2):
    return 4 * sum(
        int(math.sqrt(r2 ** 2 - y ** 2)) - math.ceil(math.sqrt(max(r1 ** 2 - y ** 2, 1))) + 1
        for y in range(r2)
    )
