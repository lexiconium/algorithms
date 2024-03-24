DENOMINATOR = int(1e9) + 7


def solution(n):
    a = b = 1

    for _ in range(n - 1):
        a, b = b, (a + b) % DENOMINATOR

    return b
