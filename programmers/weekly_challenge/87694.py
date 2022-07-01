# https://programmers.co.kr/learn/courses/30/lessons/87694


SIZE_X = 50
SIZE_Y = 50

INNER = -1
CONTOUR = 1

DX = [1, 0, -1, 0]
DY = [0, -1, 0, 1]


def overlay(rectangles):
    coordinate = [
        [0 for _ in range(2 * SIZE_Y + 1)] for _ in range(2 * SIZE_X + 1)
    ]
    for ll_x, ll_y, ur_x, ur_y in rectangles:
        ll_x *= 2
        ll_y *= 2
        ur_x *= 2
        ur_y *= 2
        for x in range(ll_x, ur_x + 1):
            for y in range(ll_y, ur_y + 1):
                if coordinate[x][y] == INNER:
                    continue

                if x == ll_x or x == ur_x or y == ll_y or y == ur_y:
                    coordinate[x][y] = CONTOUR
                else:
                    coordinate[x][y] = INNER

    return coordinate


def is_valid(x, y):
    return 0 < x < 2 * SIZE_X + 1 and 0 < y < 2 * SIZE_Y + 1


def is_path(coordinate, x, y, d):
    x += DX[d]
    y += DY[d]

    left_x = x + DX[d - 1]
    left_y = y + DY[d - 1]

    right_x = x + DX[(d + 1) % 4]
    right_y = y + DY[(d + 1) % 4]

    cond1 = is_valid(left_x, left_y) and coordinate[left_x][left_y] == INNER
    cond2 = is_valid(right_x, right_y) and coordinate[right_x][right_y] == INNER

    return cond1 + cond2 == 1


def is_contour(coordinate, x, y):
    return is_valid(x, y) and coordinate[x][y] == CONTOUR


def find_heading_directions(coordinate, initial):
    x, y = initial
    x *= 2
    y *= 2

    heading_directions = []
    for d in range(4):
        if not is_path(coordinate, x, y, d):
            continue

        nx = x + 2 * DX[d]
        ny = y + 2 * DY[d]
        if is_contour(coordinate, nx, ny):
            heading_directions.append(d)

    return heading_directions


def get_dist(coordinate, initial, destination, d):
    x, y = initial
    x *= 2
    y *= 2

    dest_x, dest_y = destination
    dest_x *= 2
    dest_y *= 2

    x += 2 * DX[d]
    y += 2 * DY[d]

    dist = 1

    while not (x == dest_x and y == dest_y):
        for _d in range(4):
            if _d ^ d == 2:
                continue
            if not is_path(coordinate, x, y, _d):
                continue

            _x = x + 2 * DX[_d]
            _y = y + 2 * DY[_d]
            if not is_contour(coordinate, _x, _y):
                continue

            x = _x
            y = _y
            d = _d
            dist += 1

            break

    return dist


def solution(rectangles, initial_x, initial_y, item_x, item_y):
    coordinate = overlay(rectangles)

    initial = (initial_x, initial_y)
    item = (item_x, item_y)

    heading_directions = find_heading_directions(coordinate, initial)
    return min(
        get_dist(coordinate, initial, item, route)
        for route in heading_directions
    )
