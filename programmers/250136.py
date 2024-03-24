from collections import deque


def solution(land):
    num_rows, num_cols = len(land), len(land[0])

    def in_bound(r, c):
        return 0 <= r < num_rows and 0 <= c < num_cols

    def get_area(board, r, c, area_id):
        board[r][c] = area_id
        q = deque([(r, c)])
        area = 1

        while q:
            r, c = q.popleft()

            for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                if not in_bound(nr := r + dr, nc := c + dc):
                    continue
                if board[nr][nc] != 1:
                    continue

                board[nr][nc] = area_id
                q.append((nr, nc))
                area += 1

        return area

    area_info = {}
    area_id = 2

    for r in range(num_rows):
        for c in range(num_cols):
            if land[r][c] != 1:
                continue

            area = get_area(land, r, c, area_id)
            area_info[area_id] = area
            area_id += 1

    return max(
        sum(
            [
                area_info[area_id]
                for area_id in {land[r][c] for r in range(num_rows) if land[r][c]}
            ],
            start=0,
        )
        for c in range(num_cols)
    )
