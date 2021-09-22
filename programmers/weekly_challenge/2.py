# https://programmers.co.kr/learn/courses/30/lessons/83201

def _grade(avg_score):
    if avg_score >= 90:
        return 'A'
    if avg_score >= 80:
        return 'B'
    if avg_score >= 70:
        return 'C'
    if avg_score >= 50:
        return 'D'
    return 'F'

def get_grade(n, score):
    score = sorted(enumerate(score), key=lambda x: x[1])
    if score[0][0] == n and score[0][1] < score[1][1]:
        return _grade(sum(map(lambda x: x[1], score[1:])) / (len(score) - 1))
    if score[-1][0] == n and score[-1][1] > score[-2][1]:
        return _grade(sum(map(lambda x: x[1], score[:-1])) / (len(score) - 1))
    return _grade(sum(map(lambda x: x[1], score)) / len(score))

def solution(scores):
    return ''.join([get_grade(n, score) for n, score in enumerate(zip(*scores))])
