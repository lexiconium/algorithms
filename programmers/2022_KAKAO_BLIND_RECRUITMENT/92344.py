# https://school.programmers.co.kr/learn/courses/30/lessons/92344


def solution(board, skill):
    prefix_sum = [
        [0 for _ in range(len(board[0]) + 1)] for _ in range(len(board) + 1)
    ]

    for t, r1, c1, r2, c2, degree in skill:
        effect = ((-1) ** t) * degree
        prefix_sum[r1][c1] += effect
        prefix_sum[r1][c2 + 1] -= effect
        prefix_sum[r2 + 1][c1] -= effect
        prefix_sum[r2 + 1][c2 + 1] += effect

    for r, row in enumerate(prefix_sum):
        prefix = 0
        for c, val in enumerate(row):
            prefix_sum[r][c] += prefix
            prefix += val

    for c in range(len(prefix_sum[0])):
        prefix = 0
        for r in range(len(prefix_sum)):
            val = prefix_sum[r][c]
            prefix_sum[r][c] += prefix
            prefix += val

    return sum(
        board[r][c] + prefix_sum[r][c] > 0
        for r in range(len(board))
        for c in range(len(board[0]))
    )
