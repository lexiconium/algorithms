import sys

sys.setrecursionlimit(200_000)


def solution(k, room_number):
    occupied = {}

    def dfs(n):
        if n not in occupied:
            occupied[n] = n + 1
            return n

        occupied[n] = dfs(occupied[n]) + 1
        return occupied[n] - 1

    return [dfs(n) for n in room_number]
