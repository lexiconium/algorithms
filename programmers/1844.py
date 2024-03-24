from collections import deque


def solution(maps):
    begin = (len(maps) - 1, len(maps[0]) - 1)
    end = (0, 0)

    q = deque([(*begin, 1)])
    visited = {begin}

    def is_valid(r, c):
        return 0 <= r < len(maps) and 0 <= c < len(maps[r]) and maps[r][c]

    while q:
        r, c, dist = q.popleft()

        if (r, c) == end:
            return dist

        for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            if not is_valid(nr := r + dr, nc := c + dc):
                continue
            if (nr, nc) in visited:
                continue

            q.append((nr, nc, dist + 1))
            visited.add((nr, nc))

    return -1
