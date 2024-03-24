# https://leetcode.com/problems/last-stone-weight-ii/


class Solution:
    # brute force 1
    def lastStoneWeightII(self, stones: list[int]) -> int:
        def dfs(weights: tuple[int]) -> int:
            if len(weights) == 1:
                return weights[0]

            return min(
                dfs(
                    weights[:i]
                    + weights[i + 1 : j]
                    + weights[j + 1 :]
                    + (abs(m - weights[j]),)
                )
                for i, m in enumerate(weights)
                for j in range(i + 1, len(weights))
            )

        return dfs(tuple(stones))

    # brute force 2
    def lastStoneWeightII(self, stones: list[int]) -> int:
        n = len(stones)
        total_weight = sum(stones)

        def get_weight(group: int) -> int:
            return sum(stones[i] for i in range(n) if (1 << i) & group)

        return min(
            abs(total_weight - 2 * get_weight(group))
            for group in range((1 << n) // 2 + 1)
        )

    # dp
    def lastStoneWeightII(self, stones: list[int]) -> int:
        total_weight = sum(stones)
        dp = {0}

        for stone in stones:
            dp |= {stone + weight for weight in dp}

        return min(abs(total_weight - 2 * weight) for weight in dp)
