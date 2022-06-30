# https://programmers.co.kr/learn/courses/30/lessons/87377


def calc_ips(lines):
    ips = []
    for i in range(len(lines) - 1):
        a, b, e = lines[i]
        for j in range(i + 1, len(lines)):
            c, d, f = lines[j]

            denominator = a * d - b * c
            if denominator == 0:
                continue

            numerator_x = b * f - e * d
            div_x, mod_x = divmod(numerator_x, denominator)
            if mod_x:
                continue

            numerator_y = e * c - a * f
            div_y, mod_y = divmod(numerator_y, denominator)
            if mod_y:
                continue

            ips.append((div_x, div_y))

    return ips


def get_box(intersection_ps):
    xs, ys = zip(*intersection_ps)
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    return (min_x, min_y), max_x - min_x + 1, max_y - min_y + 1


def transform(intersection_ps, p):
    return [(x - p[0], y - p[1]) for x, y in intersection_ps]


def draw(width, height, intersection_ps):
    canvas = [["." for _ in range(width)] for _ in range(height)]
    for x, y in intersection_ps:
        canvas[height - 1 - y][x] = "*"

    return ["".join(row) for row in canvas]


def solution(lines):
    intersection_ps = calc_ips(lines)
    lower_left_p, w, h = get_box(intersection_ps)

    box = draw(w, h, transform(intersection_ps, lower_left_p))

    return box
