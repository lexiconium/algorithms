def solution(target):
    score_info = (
        (50, 1),
        *[(s, 1) for s in range(1, 21)],
        *[(s * 2, 0) for s in range(1, 21)],
        *[(s * 3, 0) for s in range(1, 21)],
    )
    dp = [(float("inf"), float("inf")) for _ in range(target + 1)]
    dp[0] = (0, 0)

    def sum_tuples(left, right):
        return tuple(l + r for l, r in zip(left, right))

    for t in range(1, target + 1):
        for s, bull_or_single in score_info:
            if s > t:
                continue

            dp[t] = min(sum_tuples(dp[t - s], (1, -bull_or_single)), dp[t])

    num_throws, neg_num_bos = dp[target]

    return num_throws, -neg_num_bos
