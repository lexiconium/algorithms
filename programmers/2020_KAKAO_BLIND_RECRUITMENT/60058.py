# https://programmers.co.kr/learn/courses/30/lessons/60058

from collections import Counter

def is_balanced(b_list):
    cntr = Counter(b_list)
    return cntr['('] == cntr[')']

def split(p):
    u, v = [], None
    for i, b in enumerate(p, 1):
        u.append(b)
        if is_balanced(u):
            u = ''.join(u)
            v = p[i:]
            return u, v

def is_correct(p):
    stack = []
    for b in p:
        if stack and stack[-1] == '(' and b == ')':
            stack.pop()
        else:
            stack.append(b)
    return False if stack else True

def solution(p):
    if not p:
        return p
    
    u, v = split(p)
    _v = solution(v)
    if is_correct(u):
        return u + _v if _v else u
    
    return '(' + _v + ')' + ''.join(map(lambda b: '(' if b == ')' else ')', u[1:-1]))
