def solution(n):
    spent = 0

    while n:
        n, mod = divmod(n, 2)
        spent += mod

    return spent
