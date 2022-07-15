# https://school.programmers.co.kr/learn/courses/30/lessons/92341

from collections import defaultdict
from math import ceil


def solution(fees, records):
    def to_minute(t: str):
        h, m = t.split(":")
        return 60 * int(h) + int(m)

    t_end = to_minute("23:59")

    parked = defaultdict(int)
    prev_t = {}
    for record in records:
        t, car, _type = record.split()
        t = to_minute(t)
        car = int(car)

        if _type == "IN":
            prev_t[car] = t
        else:
            parked[car] += t - prev_t[car]
            prev_t.pop(car)

    for car, t in prev_t.items():
        parked[car] += t_end - t

    def calculate_fee(t: int):
        if t <= fees[0]:
            return fees[1]

        return fees[1] + fees[3] * ceil((t - fees[0]) / fees[2])

    return [calculate_fee(parked[car]) for car in sorted(parked.keys())]
