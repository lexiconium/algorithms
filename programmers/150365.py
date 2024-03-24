from collections import deque


def solution(n, m, x, y, r, c, k):
    def is_valid(r, c):
        return 0 < r <= n and 0 < c <= m

    q = deque([("", x, y)])

    while q:
        path, i, j = q.popleft()

        if len(path) > k:
            return "impossible"

        if (i, j) == (r, c):
            if len(path) == k:
                return path

            if (k - len(path)) % 2:
                return "impossible"

        for d, di, dj in (("d", 1, 0), ("l", 0, -1), ("r", 0, 1), ("u", -1, 0)):
            if not is_valid(ni := i + di, nj := j + dj):
                continue

            if len(path) + 1 + abs(r - ni) + abs(c - nj) > k:
                continue

            q.append((path + d, ni, nj))
            break

    return "impossible"
