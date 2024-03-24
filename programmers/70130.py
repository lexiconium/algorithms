from collections import Counter
from functools import lru_cache


# TLE
def solution(a):
    @lru_cache(None)
    def longest_star_sequence(lbound=0, ubound=len(a)):
        if ubound - lbound == 1:
            return 0, set()

        if ubound - lbound == 2:
            comps = set(a[lbound:ubound])

            if len(comps) == 1:
                return 0, set()

            return 2, comps

        longest_len = 0
        comps = set()

        for i in range(lbound + 1, ubound):
            left_len, left_comps = longest_star_sequence(lbound, i)
            right_len, right_comps = longest_star_sequence(i, ubound)

            if inter_comps := left_comps.intersection(right_comps):
                if left_len + right_len > longest_len:
                    longest_len = left_len + right_len
                    comps = inter_comps

                continue

            if left_len > longest_len:
                longest_len = left_len
                comps = left_comps

            if right_len > longest_len:
                longest_len = right_len
                comps = right_comps

        return longest_len, comps

    return longest_star_sequence()[0]


def solution(a):
    num_counter = Counter(a)

    max_half_len = 0

    for num, cnt in num_counter.items():
        if cnt < max_half_len:
            continue

        i = 1
        half_len = 0

        while i < len(a):
            if a[i - 1] != num and a[i] != num or a[i - 1] == a[i]:
                i += 1
                continue

            i += 2
            half_len += 1

        max_half_len = max(half_len, max_half_len)

    return max_half_len * 2
