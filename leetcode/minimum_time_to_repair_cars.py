# https://leetcode.com/problems/minimum-time-to-repair-cars/description/


from collections import Counter


class Solution:
    def repairCars(self, ranks: list[int], cars: int) -> int:
        min_t, max_t = 1, min(ranks) * cars**2

        rank_counter = Counter(ranks)

        while min_t < max_t:
            t = (min_t + max_t) // 2
            num_repaired = sum(n * int((t / r) ** 0.5) for r, n in rank_counter.items())

            if num_repaired < cars:
                min_t = t + 1
            else:
                max_t = t

        return min_t
