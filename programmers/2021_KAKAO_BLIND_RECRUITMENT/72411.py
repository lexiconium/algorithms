# https://programmers.co.kr/learn/courses/30/lessons/72411

from collections import Counter
from itertools import combinations

def solution(orders, course):
    menu = []
    for n in course:
        ordered = []
        for order in orders:
            ordered += combinations(sorted(order), n)
        menucnt = Counter(ordered)
        menu += [''.join(m) for m in menucnt if menucnt[m] > 1 and menucnt[m] == max(menucnt.values())]
    return sorted(menu)
