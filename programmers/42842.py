def solution(brown, yellow):
    return [
        w := (brown // 2 + 2 + ((brown // 2 + 2) ** 2 - 4 * (brown + yellow)) ** 0.5) // 2,
        brown // 2 + 2 - w
    ]
