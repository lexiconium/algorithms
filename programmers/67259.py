from collections import deque


def solution(board):
    n = len(board)
    min_costs = [[[float("inf") for _ in range(4)] for _ in row] for row in board]

    q = deque([(0, 0, -1, 0)])

    for d in range(4):
        min_costs[0][0][d] = 0

    def in_bound(r, c):
        return 0 <= r < n and 0 <= c < n

    while q:
        r, c, prev_d, cost = q.popleft()

        for d, (dr, dc) in enumerate([(-1, 0), (0, 1), (1, 0), (0, -1)]):
            if not in_bound(nr := r + dr, nc := c + dc):
                continue
            if board[nr][nc]:
                continue
            if min_costs[nr][nc][d] <= (ncost := cost + (100 if prev_d == -1 or d == prev_d else 600)):
                continue

            min_costs[nr][nc][d] = ncost
            q.append((nr, nc, d, ncost))

    return min(min_costs[-1][-1])
