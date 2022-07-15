# https://school.programmers.co.kr/learn/courses/30/lessons/92342


def solution(n, info):
    global max_diff, max_diff_shot

    def calc_diff(shot):
        diff = 0
        for idx in range(11):
            if shot[idx] > info[idx]:
                diff += 10 - idx
            elif info[idx]:
                diff -= 10 - idx

        return diff if diff > 0 else -1

    def dfs(remaining, idx, shot):
        global max_diff, max_diff_shot

        if not remaining:
            diff = calc_diff(shot)
            if diff > max_diff:
                max_diff = diff
                max_diff_shot = shot[:]
            return

        if idx == -1:
            return

        shot[idx] += 1
        dfs(remaining - 1, idx, shot)
        shot[idx] -= 1
        dfs(remaining, idx - 1, shot)

    max_diff = -1
    max_diff_shot = [-1]

    dfs(n, 10, [0 for _ in info])

    return max_diff_shot
