# https://leetcode.com/problems/maximum-length-of-pair-chain/


class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        pairs = sorted(pairs)

        dp = [1] * (n := len(pairs))
        longest = 1

        for i in reversed(range(n - 1)):
            dp[i] = max(
                (dp[j] + 1) * (pairs[i][1] < pairs[j][0])
                for j in range(i + 1, n)
            )
            longest = max(dp[i], longest)

        return longest

    def findLongestChain(self, pairs: list[list[int]]) -> int:
        prev_end = -1001
        longest = 0

        for begin, end in sorted(pairs, key=lambda p: p[1]):
            if begin <= prev_end:
                continue

            prev_end = end
            longest += 1

        return longest
