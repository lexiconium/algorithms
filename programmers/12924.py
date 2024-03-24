def solution(n):
    return sum(
        n % m == (0 if m % 2 else m // 2)
        for m in range(1, int((-1 + (1 + 8 * n) ** 0.5) / 2) + 1)
    )
