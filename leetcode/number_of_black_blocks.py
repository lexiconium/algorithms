# https://leetcode.com/problems/number-of-black-blocks/description/

from collections import defaultdict


class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: list[list[int]]) -> list[int]:
        num_blacks_in_block = defaultdict(int)

        def is_valid(r: int, c: int) -> bool:
            return 0 <= r < m - 1 and 0 <= c < n - 1

        for r, c in coordinates:
            for dr, dc in ((-1, -1), (0, -1), (0, 0), (-1, 0)):
                if not is_valid(r + dr, c + dc):
                    continue

                num_blacks_in_block[r + dr, c + dc] += 1

        counter = [0] * 5
        for num_blacks in num_blacks_in_block.values():
            counter[num_blacks] += 1

        counter[0] = (m - 1) * (n - 1) - sum(counter)

        return counter
