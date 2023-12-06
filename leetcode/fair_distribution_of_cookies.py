# https://leetcode.com/problems/fair-distribution-of-cookies/description/

from functools import cache


class Solution:
    def distributeCookies(self, cookies: list[int], k: int) -> int:
        num_cookies = len(cookies)

        @cache
        def sum_cookies(picked: int) -> int:
            return sum(cookies[i] for i in range(num_cookies) if (1 << i) & picked)

        @cache
        def dfs(available: int, num_to_pick: int) -> int:
            if num_to_pick == 1:
                return sum_cookies(available)

            return min(
                [max(sum_cookies(picked), dfs(available - picked, num_to_pick - 1))
                 for picked in range(1, available)
                 if (picked & available) == picked],
                default=float("inf")
            )

        return dfs((1 << num_cookies) - 1, k)
