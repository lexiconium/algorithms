# https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/

import math


class Solution:
    def minimizedMaximum(self, n: int, quantities: list[int]) -> int:
        lower = math.ceil(sum(quantities) / n)
        upper = max(quantities)

        def stores_needed(n_per: int) -> int:
            return sum(math.ceil(q / n_per) for q in quantities)

        while lower < upper:
            if stores_needed(mid := (lower + upper) // 2) > n:
                lower = mid + 1
            else:
                upper = mid

        return lower
