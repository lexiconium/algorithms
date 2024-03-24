MOD_TO_124 = ("1", "2", "4")


def solution(n):
    converted = []

    while n:
        n, mod = divmod(n - 1, 3)
        converted.append(MOD_TO_124[mod])

    return "".join(reversed(converted))
