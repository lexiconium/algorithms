# https://programmers.co.kr/learn/courses/30/lessons/87946

from itertools import permutations


def solution(k, dungeons):
    max_cnt = 0
    for permutation in permutations(dungeons, len(dungeons)):
        t = k
        cnt = 0
        for t_needed, _t in permutation:
            if t_needed > t:
                break
            t -= _t
            cnt += 1

        max_cnt = max(max_cnt, cnt)

    return max_cnt
