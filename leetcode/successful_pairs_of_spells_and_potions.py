# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/


import bisect


class Solution:
    def successfulPairs(
        self, spells: list[int], potions: list[int], success: int
    ) -> list[int]:
        potions = sorted(potions)
        m = len(potions)

        cache = {}
        pairs = []

        for spell in spells:
            if spell not in cache:
                cache[spell] = m - bisect.bisect_left(
                    potions, (success + spell - 1) // spell
                )

            pairs.append(cache[spell])

        return pairs
