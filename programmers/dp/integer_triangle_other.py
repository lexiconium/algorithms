# https://programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle, layer=[]):
    return solution(triangle[1:], [max(left, right) + n for left, right, n in zip(layer + [0], [0] + layer, triangle[0])]) if triangle else max(layer)
