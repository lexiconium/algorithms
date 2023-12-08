# https://leetcode.com/problems/stone-game
# https://leetcode.com/problems/stone-game/solutions/154610/dp-or-just-return-true

class Solution:
    def stoneGame(self, _: list[int]) -> bool:
        return True

    # generalized
    def stoneGame(self, piles: list[int]) -> bool:
        num_rows = len(piles)

        dp = [[0] * num_rows for _ in piles]

        for i, n in enumerate(piles):
            dp[i][i] = n

        for begin in reversed(range(num_rows - 1)):
            for end in range(begin + 1, num_rows):
                dp[begin][end] = max(
                    piles[begin] - dp[begin + 1][end],
                    piles[end] - dp[begin][end - 1]
                )

        return dp[0][-1] > 0
