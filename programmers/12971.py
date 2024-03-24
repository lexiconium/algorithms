def solution(sticker):
    if len(sticker) < 4:
        return max(sticker)

    dp_0 = [0] + [n for n in sticker]
    dp_0[-1] = 0

    for i in range(2, len(dp_0)):
        dp_0[i] = max(dp_0[i] + dp_0[i - 2], dp_0[i - 1])

    dp_1 = [n for n in sticker]
    dp_1[0] = 0

    for i in range(2, len(dp_1)):
        dp_1[i] = max(dp_1[i] + dp_1[i - 2], dp_1[i - 1])

    return max(dp_0[-1], dp_1[-1])
