def solution(matrix_sizes):
    dp = [[0 for _ in matrix_sizes] for _ in matrix_sizes]

    for i in reversed(range(len(matrix_sizes) - 1)):
        for j in range(i + 1, len(matrix_sizes)):
            dp[i][j] = min(
                dp[i][k] + matrix_sizes[i][0] * matrix_sizes[k][1] * matrix_sizes[j][1] + dp[k + 1][j]
                for k in range(i, j)
            )

    return dp[0][-1]
