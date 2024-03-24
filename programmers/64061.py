def solution(board, moves):
    board = [list(filter(lambda doll: doll > 0, column))[::-1] for column in zip(*board)]
    stack = []
    cnt = 0

    for c in map(lambda n: n - 1, moves):
        if not board[c]:
            continue

        doll = board[c].pop()

        if not stack or stack[-1] != doll:
            stack.append(doll)
        else:
            stack.pop()
            cnt += 1

    return cnt
