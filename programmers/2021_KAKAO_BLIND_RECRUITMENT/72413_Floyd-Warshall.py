# https://programmers.co.kr/learn/courses/30/lessons/72413#

import heapq

def solution(n, s, a, b, fares):
    dp = [[float('inf') for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0
    for i, j, cost in fares:
        dp[i - 1][j - 1] = dp[j - 1][i - 1] = cost
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if dp[j][k] > dp[j][i] + dp[i][k]:
                    dp[j][k] = dp[j][i] + dp[i][k]
    
    min_cost = float('inf')
    for i in range(n):
        min_cost = min(dp[s - 1][i] + dp[i][a - 1] + dp[i][b - 1], min_cost)
    
    return min_cost