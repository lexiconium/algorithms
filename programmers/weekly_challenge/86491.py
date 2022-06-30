# https://programmers.co.kr/learn/courses/30/lessons/86491


def preprocess(sizes):
    return [(w, h) if w > h else (h, w) for w, h in sizes]


def solution(sizes):
    widths, heights = map(sorted, zip(*preprocess(sizes)))
    return widths[-1] * heights[-1]
