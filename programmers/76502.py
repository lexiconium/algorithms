from collections import deque


def does_match(l, r):
    return l == "(" and r == ")" or l == "{" and r == "}" or l == "[" and r == "]"


def solution(s):
    if len(s) % 2:
        return 0

    cnt = 0

    for i in range(len(s := deque(s))):
        s.rotate()

        stack = []

        for p in s:
            if stack and does_match(stack[-1], p):
                stack.pop()
            else:
                stack.append(p)

        if not stack:
            cnt += 1

    return cnt
