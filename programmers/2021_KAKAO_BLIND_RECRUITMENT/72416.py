# https://programmers.co.kr/learn/courses/30/lessons/72416

from collections import defaultdict

visited = set()
tree = defaultdict(list)

def sum_upstream(n, dp, sales):
    dp[n][0] = sales[n - 1]
    visited.add(n)
    
    if not tree[n]:
        return
    
    for member in tree[n]:
        if member not in visited:
            sum_upstream(member, dp, sales)
            dp[n][0] += min(dp[member])
    
    without_chief_sum = 0
    is_there_member = False
    tmp = []
    for member in tree[n]:
        if dp[member][0] < dp[member][1]:
            without_chief_sum += dp[member][0]
            is_there_member = True
        else:
            without_chief_sum += dp[member][1]
            tmp.append(dp[member][0] - dp[member][1])
    
    dp[n][1] = without_chief_sum
    if not is_there_member:
        dp[n][1] += sorted(tmp)[0] # make at least one member to attend

def solution(sales, links):
    dp = [[0, 0] for _ in range(len(sales) + 1)]
    for chief, member in links:
        tree[chief].append(member)
    
    sum_upstream(1, dp, sales)
    return min(dp[1])
