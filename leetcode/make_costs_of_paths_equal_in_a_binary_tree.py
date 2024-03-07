# https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree


class Solution:
    # https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree/solutions/3494915/java-c-python-bottom-up-and-follow-up/
    def minIncrements(self, n: int, cost: list[int]) -> int:
        num_increments = 0

        for i in reversed(range(n // 2)):
            num_increments += abs(
                (left := cost[2 * i + 1]) - (right := cost[2 * i + 2])
            )
            cost[i] += max(left, right)

        return num_increments
