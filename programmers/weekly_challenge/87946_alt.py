# https://programmers.co.kr/learn/courses/30/lessons/87946

def solution(k, dungeons):
    if not dungeons:
        return 0

    return max([
        solution(k - used, dungeons[:i] + dungeons[i + 1:]) + 1
        for i, (required, used) in enumerate(dungeons)
        if k >= required
    ], default=0)
