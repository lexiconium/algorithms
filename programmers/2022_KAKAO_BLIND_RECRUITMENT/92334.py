# https://school.programmers.co.kr/learn/courses/30/lessons/92334

from collections import defaultdict


def solution(id_list, reports, k):
    who_reported_whom = defaultdict(set)
    for report in reports:
        who, reported = report.split()
        who_reported_whom[who].add(reported)

    reported_cnt = defaultdict(int)
    for reported_set in who_reported_whom.values():
        for reported in reported_set:
            reported_cnt[reported] += 1

    banned = set()
    for reported, cnt in reported_cnt.items():
        if cnt < k:
            continue
        banned.add(reported)

    return [len(who_reported_whom[_id] & banned) for _id in id_list]
