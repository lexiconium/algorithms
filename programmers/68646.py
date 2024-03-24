def solution(a):
    right_mins = [float("inf")]

    for n in reversed(a):
        right_mins.append(min(right_mins[-1], n))

    left_min = float("inf")
    cnt = 0

    for i, n in enumerate(a, 2):
        if n < left_min or n < right_mins[-i]:
            cnt += 1

        left_min = min(left_min, n)

    return cnt
