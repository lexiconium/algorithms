def solution(s):
    stack = []

    for p in s:
        if not stack and p == ")":
            return False

        if stack and stack[-1] == "(" and p == ")":
            stack.pop()
            continue

        stack.append(p)

    return not stack
