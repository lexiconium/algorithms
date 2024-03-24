DENOMINATOR = 1234567


def solution(n):
    a = b = 1

    for _ in range(n - 1):
        a, b = b, (a + b)

    return b % DENOMINATOR
