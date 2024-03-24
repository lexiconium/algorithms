DIV = int(1e9) + 7


def solution(n, money):
    dp = [0] * (n + 1)

    for m in sorted(money):
        dp[m] += 1

        for change in range(m + 1, n + 1):
            dp[change] += dp[change - m] % DIV

    return dp[-1] % DIV
