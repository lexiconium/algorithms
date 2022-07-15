# https://school.programmers.co.kr/learn/courses/30/lessons/92342


from copy import copy


def solution(n, info):
    def calc_diff(shot):
        ryan = 0
        apeach = 0
        for idx in range(11):
            if shot[idx] > info[idx]:
                ryan += 10 - idx
            elif info[idx]:
                apeach += 10 - idx

        return ryan - apeach if ryan > apeach else -1

    def dfs(remaining, shot, idx=0):
        if not remaining:
            diff = calc_diff(shot)
            return diff, (copy(shot) if diff > -1 else [-1])

        if idx == n + 1:
            return -1, [-1]

        diff1, shot1 = dfs(remaining, shot, idx + 1)

        shot[idx] += 1
        diff2, shot2 = dfs(remaining - 1, shot, idx)
        shot[idx] -= 1

        if diff1 > diff2:
            return diff1, shot1
        elif diff2 > diff1:
            return diff2, shot2
        elif diff1 > -1:
            for rev_idx in range(11)[::-1]:
                if shot1[rev_idx] == shot2[rev_idx]:
                    continue
                if shot1[rev_idx] > shot2[rev_idx]:
                    return diff1, shot1
                return diff2, shot2

        return -1, [-1]

    return dfs(n, [0 for _ in info])[1]
