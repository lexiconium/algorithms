# https://www.acmicpc.net/problem/14500

DR = [-1, 0, 1, 0]
DC = [0, 1, 0, -1]

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
max_value = max(max(row) for row in board)

max_sum = 0


def is_valid(r: int, c: int, d: int):
    return 0 <= r + DR[d] < m and 0 <= c + DC[d] < n


def dfs(r: int, c: int, d: int = -1, _sum: int = 0, len_left: int = 4):
    global max_sum

    if _sum + len_left * max_value <= max_sum:
        return

    if not len_left:
        max_sum = max(max_sum, _sum)
        return

    for _d in range(4):
        if _d ^ d == 2:
            continue
        if not is_valid(r, c, _d):
            continue

        dfs(r + DR[_d], c + DC[_d], _d, _sum + board[r][c], len_left - 1)

        if len_left == 3:
            for d_ in range(_d + 1, 4):
                if d_ ^ d == 2:
                    continue
                if not is_valid(r, c, d_):
                    continue

                max_sum = max(
                    max_sum,
                    _sum
                    + board[r][c]
                    + board[r + DR[_d]][c + DC[_d]]
                    + board[r + DR[d_]][c + DC[d_]],
                )


for r in range(m):
    for c in range(n):
        dfs(r, c)

print(max_sum)
