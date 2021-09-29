# https://programmers.co.kr/learn/courses/30/lessons/43162

def solution(n, computers):
    dj_set = [m for m in range(n)]
    for i, others in enumerate(computers):
        for j, is_connected in enumerate(others):
            if i == j or not is_connected:
                continue

            if dj_set[i] != dj_set[j]:
                if dj_set[i] > dj_set[j]:
                    dj_set[i] = dj_set[j]
                else:
                    dj_set[j] = dj_set[i]

    return len(set(dj_set))
