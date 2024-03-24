from collections import deque


def get_p_locs(room):
    return [(r, c) for r, row in enumerate(room) for c, s in enumerate(row) if s == "P"]


def calc_dist(loc_1, loc_2):
    return abs(loc_1[0] - loc_2[0]) + abs(loc_1[1] - loc_2[1])


def is_partitioned(loc_1, loc_2, room):
    q = deque([(*loc_1, calc_dist(loc_1, loc_2))])
    visited = {loc_1}

    def valid(r, c):
        return 0 <= r < len(room) and 0 <= c < len(room[0])

    while q:
        r, c, d = q.popleft()

        if (r, c) == loc_2:
            return False

        for dr, dc in ((0, 1), (1, 0), (0, -1)):
            if not valid(nr := r + dr, nc := c + dc):
                continue
            if room[nr][nc] == "X":
                continue
            if (nd := calc_dist(nloc := (nr, nc), loc_2)) > d:
                continue
            if nloc in visited:
                continue

            q.append((nr, nc, nd))
            visited.add(nloc)

    return True


def is_distanced(room):
    p_locs = get_p_locs(room)

    for i in range(len(p_locs) - 1):
        for j in range(i + 1, len(p_locs)):
            if calc_dist(p_locs[i], p_locs[j]) > 2:
                continue
            if is_partitioned(p_locs[i], p_locs[j], room):
                continue

            return 0
    return 1


def solution(places):
    return [is_distanced(room) for room in places]
