# https://programmers.co.kr/learn/courses/30/lessons/72414

def solution(play_time, adv_time, logs):
    t2sec = lambda t: 3600 * int(t[:2]) + 60 * int(t[3:5]) + int(t[6:])
    
    play_len = t2sec(play_time)
    dp = [0 for _ in range(play_len)]
    
    for log in logs:
        start, end = map(t2sec, log.split('-'))
        dp[start] += 1
        if end < play_len:
            dp[end] -= 1
    
    for t in range(play_len - 1):
        dp[t + 1] += dp[t]
    
    adv_len = t2sec(adv_time)
    max_play = _sum = sum(dp[:adv_len])
    start = 0
    for t in range(adv_len, play_len):
        _sum += dp[t] - dp[t - adv_len]
        if _sum > max_play:
            max_play = _sum
            start = t - adv_len + 1
    
    return f'{start // 3600:02d}:{(start % 3600) // 60:02d}:{start % 60:02d}'
