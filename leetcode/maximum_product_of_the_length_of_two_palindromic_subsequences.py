# https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/

from functools import cache


class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        num_masks = 1 << n

        @cache
        def max_palindrome_len(mask: int) -> int:
            if not mask:
                return 0

            sub_s = "".join(c for i, c in enumerate(s) if (1 << i) & mask)

            if sub_s == sub_s[::-1]:
                return len(sub_s)

            return max(
                max_palindrome_len(mask - (1 << i)) for i in range(n) if (1 << i) & mask
            )

        return max(
            max_palindrome_len(mask) * max_palindrome_len(num_masks - 1 - mask)
            for mask in range(num_masks // 2)
        )
