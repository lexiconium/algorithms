MOD = int(1e9) + 7


def solution(n):
    if n % 2:
        return 0

    complete, incomplete = 1, 0

    for _ in range(n // 2):
        complete, incomplete = (3 * complete + incomplete) % MOD, (
            2 * complete + incomplete
        ) % MOD

    return complete
