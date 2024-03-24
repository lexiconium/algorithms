def solution(numbers, hand):
    npos = {
        n + 1: (n // 3, n % 3, "n" if n % 3 == 1 else ("l" if n % 3 == 0 else "r"))
        for n in range(9)
    }
    npos[0] = (3, 1, "n")

    pressed_with = []

    def dist(p_1, p_2):
        return abs(p_1[0] - p_2[0]) + abs(p_1[1] - p_2[1])

    lpos, rpos = (3, 0), (3, 2)

    for n in numbers:
        *p, side = npos[n]

        if side == "n":
            if (ld := dist(lpos, p)) == (rd := dist(rpos, p)):
                side = "l" if hand == "left" else "r"
            elif ld < rd:
                side = "l"
            else:
                side = "r"

        if side == "l":
            lpos = p
        else:
            rpos = p

        pressed_with.append(side.upper())

    return "".join(pressed_with)
