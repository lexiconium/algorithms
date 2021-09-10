# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    min_len = len(s)
    for k in range(1, len(s) // 2 + 1):
        divided = [s[start:start + k] for start in range(0, len(s), k)]
        result = [1, divided[0]]
        for i in range(1, len(divided)):
            if divided[i] == result[-1]:
                result[-2] += 1
            else:
                result.append(1)
                result.append(divided[i])
        result = ''.join(map(lambda x: '' if x == 1 else str(x), result))
        min_len = min(min_len, len(result))
    return min_len
