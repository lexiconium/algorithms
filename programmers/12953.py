import math
from functools import reduce


def solution(arr):
    return reduce(lambda left, right: left * right // math.gcd(left, right), arr)
