from math import ceil


def solution(n, stations, w):
    cnt = 0

    for i in range(len(stations) + 1):
        if i == 0:
            left, right = 0, stations[i] - w
        elif i == len(stations):
            left, right = stations[i - 1] + w, n
        else:
            left, right = stations[i - 1] + w, stations[i] - w

        if (num_blocks := right - left - 1) <= 0:
            continue

        cnt += ceil(num_blocks / (2 * w))

    return cnt
