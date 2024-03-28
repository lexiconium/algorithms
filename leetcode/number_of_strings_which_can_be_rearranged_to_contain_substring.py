# https://leetcode.com/problems/number-of-strings-which-can-be-rearranged-to-contain-substring/description/

from functools import cache

MOD = int(1e9) + 7


class Solution:
    # math
    def stringCount(self, n: int) -> int:
        if n < 4:
            return 0

        number_of_cases = pow(26, n, MOD)
        to_exclude = 0

        # exclude (i) U (ii) U (iii) from total number of cases where:
        # (i) n(e) in {0, 1}
        # (ii) n(l) = 0
        # (iii) n(t) = 0

        # (i) + (ii) + (iii)
        to_exclude += (3 * pow(25, n, MOD) + n * pow(25, n - 1, MOD)) % MOD

        # (i) and (ii) + (ii) and (iii) + (iii) and (i)
        to_exclude -= (3 * pow(24, n, MOD) + 2 * n * pow(24, n - 1, MOD)) % MOD

        # (i) and (ii) and (iii)
        to_exclude += (pow(23, n, MOD) + n * pow(23, n - 1, MOD)) % MOD

        return (number_of_cases - to_exclude) % MOD

    # memoization
    def stringCount(self, n: int) -> int:
        fulfilled = (1 << 4) - 1

        @cache
        def dfs(i: int = 0, mask: int = 0) -> int:
            if i == n:
                return int(mask == fulfilled)

            # l or t
            cnt = dfs(i + 1, mask | 1 << 3) + dfs(i + 1, mask | 1)

            # check e is met before
            cnt += dfs(i + 1, mask | ((1 << 2) if mask & (1 << 1) else (1 << 1)))

            # other 23 characters
            cnt += 23 * dfs(i + 1, mask)

            return cnt % MOD

        return dfs()
