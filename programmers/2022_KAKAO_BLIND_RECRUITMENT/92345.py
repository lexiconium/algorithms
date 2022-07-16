# https://school.programmers.co.kr/learn/courses/30/lessons/92345


def solution(board, aloc, bloc):
    def valid(r, c):
        return 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c]

    def adjacent(r, c):
        yield from [
            (r + dr, c + dc)
            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]
            if valid(r + dr, c + dc)
        ]

    def dfs(aloc, bloc, *, aturn=True):
        r, c = aloc if aturn else bloc
        if not board[r][c]:
            return False, 0

        can_i_win = False
        max_depth = 0
        min_depth = float("inf")

        board[r][c] = 0

        for nloc in adjacent(r, c):
            can_opponent_win, depth = dfs(
                nloc if aturn else aloc,
                nloc if not aturn else bloc,
                aturn=not aturn,
            )
            if can_opponent_win:
                max_depth = max(max_depth, depth + 1)
            else:
                min_depth = min(min_depth, depth + 1)

            can_i_win |= not can_opponent_win

        board[r][c] = 1

        return (
            bool(can_i_win),
            (min_depth if can_i_win else max_depth),
        )

    return dfs(aloc, bloc)[1]
