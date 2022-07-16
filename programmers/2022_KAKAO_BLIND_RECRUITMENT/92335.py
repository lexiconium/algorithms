# https://school.programmers.co.kr/learn/courses/30/lessons/92335


def convert(n: int, k: int):
    if k == 10:
        return n

    digits = []
    while n >= k:
        n, digit = divmod(n, k)
        digits.append(str(digit))

    digits.append(str(n))

    return int("".join(digits[::-1]))


def is_prime(n: int):
    if n == 1:
        return False

    for denominator in range(2, int(n ** 0.5) + 1):
        if n % denominator == 0:
            return False

    return True


def solution(n, k):
    return sum(
        is_prime(num)
        for num in map(
            int, filter(lambda num: len(num), str(convert(n, k)).split("0"))
        )
    )
