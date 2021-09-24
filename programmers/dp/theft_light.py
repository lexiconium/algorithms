# https://programmers.co.kr/learn/courses/30/lessons/42897

def solution(money):
    stole0_pprev = stole0_prev = money[0]
    stole1_pprev, stole1_prev = 0, money[1]
    for m in money[2:]:
        stole0_pprev, stole0_prev = stole0_prev, max(stole0_prev, stole0_pprev + m)
        stole1_pprev, stole1_prev = stole1_prev, max(stole1_prev, stole1_pprev + m)
    
    return max(stole0_pprev, stole1_prev)