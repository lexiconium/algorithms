# https://leetcode.com/problems/domino-and-tromino-tiling/


MOD = int(1e9) + 7


class Solution:
    # brute force
    def numTilings(self, n: int) -> int:
        def dfs(i: int = 0, complete: bool = True) -> int:
            if i > n:
                return 0
            if i == n:
                return int(complete)

            if complete:
                # vertical domino + stacked horizontal dominos + 2 * tromino
                return (
                    dfs(i + 1, True) + dfs(i + 2, True) + 2 * dfs(i + 2, False)
                ) % MOD
            # horizontal domino + tromino
            return (dfs(i + 1, False) + dfs(i + 1, True)) % MOD

        return dfs()

    # tabulation
    def numTilings(self, n: int) -> int:
        dp = [[0, 0] for _ in range(n + 1)]

        dp[0] = [1, 0]
        dp[1] = [1, 0]

        for m in range(2, n + 1):
            # stacked horizontal dominos + vertical domino + tromino
            dp[m][0] = (dp[m - 2][0] + dp[m - 1][0] + dp[m - 1][1]) % MOD
            # 2 * tromino + horizontal domino
            dp[m][1] = (2 * dp[m - 2][0] + dp[m - 1][1]) % MOD

        return dp[-1][0]
