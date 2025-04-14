# https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/description/


class Solution:
    def maxCollectedFruits(self, fruits: list[list[int]]) -> int:
        for i in range(n := len(fruits)):
            for j in range(n):
                # the top triangle cannot be reached by (0, n - 1) child
                if i < j < n - 1 - i:
                    fruits[i][j] = 0

                # the left triangle cannot be reached by (n - 1, 0) child
                if j < i < n - 1 - j:
                    fruits[i][j] = 0

        # diag
        for i in range(1, n):
            fruits[i][i] += fruits[i - 1][i - 1]

        # triu
        for i in range(1, n):
            for j in range(i + 1, n):
                fruits[i][j] += max(
                    fruits[i - 1][j - 1],
                    fruits[i - 1][j],
                    fruits[i - 1][j + 1] if j != n - 1 else 0,
                )

        fruits[-1][-1] += fruits[-2][-1]

        # tril
        for j in range(1, n):
            for i in range(j + 1, n):
                fruits[i][j] += max(
                    fruits[i - 1][j - 1],
                    fruits[i][j - 1],
                    fruits[i + 1][j - 1] if i != n - 1 else 0,
                )

        fruits[-1][-1] += fruits[-1][-2]

        return fruits[-1][-1]
