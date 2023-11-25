# https://leetcode.com/problems/shopping-offers/
# https://leetcode.com/problems/shopping-offers/discuss/105252/Concise-c%2B%2B-DFS-solution-6ms

# time complexity:

from functools import cache

class Solution:
    def shoppingOffers(self, price: list[int], special: list[list[int]], needs: list[int]) -> int:
        def sub(a, b): return tuple([n - b[i] for i, n in enumerate(a)])

        @cache
        def dfs(_needs: tuple[int]) -> int:
            if any(n < 0 for n in _needs):
                return float('inf')

            _min = sum(price[i] * n for i, n in enumerate(_needs))
            for offer in special:
                if offer[-1] < _min:
                    _min = min(_min, offer[-1] + dfs(sub(_needs, offer)))
            return _min
        return dfs(tuple(needs))