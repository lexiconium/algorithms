def solution(n, a, b):
    return ((a - 1) ^ (b - 1)).bit_length()
