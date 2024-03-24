def solution(board):
    for r in range(1, len(board)):
        for c in range(1, len(board[0])):
            if not board[r][c]:
                continue

            board[r][c] = min(
                board[r - 1][c - 1],
                board[r - 1][c],
                board[r][c - 1]
            ) + 1

    return max(max(row) for row in board) ** 2
