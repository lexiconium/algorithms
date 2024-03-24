def solution(land):
    for r in range(1, len(land)):
        for c in range(4):
            land[r][c] += max(land[r - 1][prev_c] for prev_c in range(4) if prev_c != c)

    return max(land[-1])
