from functools import lru_cache


def solution(arr):
    def op(left, right, op_str):
        if op_str == "+":
            return left + right
        return left - right

    @lru_cache(None)
    def dfs(n_and_op, max_or_min=max):
        if len(n_and_op) == 1:
            return int(n_and_op[0])
        return max_or_min(
            op(
                dfs(n_and_op[: i - 1], max_or_min),
                dfs(
                    n_and_op[i:],
                    (
                        max_or_min
                        if n_and_op[i - 1] == "+"
                        else (min if max_or_min == max else max)
                    ),
                ),
                n_and_op[i - 1],
            )
            for i in range(2, len(n_and_op), 2)
        )

    return dfs(tuple(arr))


# dp
def solution(arr):
    nums = [int(arr[i]) for i in range(0, len(arr), 2)]
    ops = arr[1::2]

    n = len(nums)
    dp = [[(0, 0) for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = (nums[i], nums[i])

    for length in range(2, n + 1):
        for start in range(n - length + 1):
            end = start + length - 1
            min_val, max_val = float("inf"), float("-inf")
            for k in range(start, end):
                left_min, left_max = dp[start][k]
                right_min, right_max = dp[k + 1][end]
                if ops[k] == "+":
                    min_val = min(min_val, left_min + right_min)
                    max_val = max(max_val, left_max + right_max)
                else:
                    min_val = min(min_val, left_min - right_max)
                    max_val = max(max_val, left_max - right_min)
            dp[start][end] = (min_val, max_val)

    return dp[0][n - 1][1]
