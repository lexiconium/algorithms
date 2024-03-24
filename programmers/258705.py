def solution(n, tops):
    dp = [[0, 0] for _ in range(len(tops) + 1)]
    dp[0][0] = 1

    mod = 10_007

    for i, top in enumerate(tops, 1):
        # previous cases should not include the case
        # ends (bottom right) with triangle
        dp[i][0] = (dp[i - 1][0] * (2 + top) + dp[i - 1][1] * (1 + top)) % mod
        dp[i][1] = (dp[i - 1][0] + dp[i - 1][1]) % mod

    return sum(dp[-1]) % mod
