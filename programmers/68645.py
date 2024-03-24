def solution(n):
    lower_triangle = [[0 for _ in range(n)] for _ in range(n)]

    dr = (1, 0, -1)
    dc = (0, 1, -1)

    r = c = d = 0

    def is_valid(r, c):
        return 0 <= r < n and 0 <= c < n and lower_triangle[r][c] == 0

    for num in range(n * (n + 1) // 2):
        lower_triangle[r][c] = num + 1

        if not is_valid(nr := r + dr[d], nc := c + dc[d]):
            d = (d + 1) % 3
            nr, nc = r + dr[d], c + dc[d]

        r, c = nr, nc

    return [num for row in lower_triangle for num in filter(lambda num: num > 0, row)]
