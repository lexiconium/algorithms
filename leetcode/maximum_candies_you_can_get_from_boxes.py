# https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/description/


class Solution:
    def maxCandies(
        self,
        status: list[int],
        candies: list[int],
        keys: list[list[int]],
        containedBoxes: list[list[int]],
        initialBoxes: list[int],
    ) -> int:
        boxes = set(initialBoxes)

        key_set = set()
        for box in boxes:
            if status[box]:
                key_set |= set(keys[box])

        num_candies = 0
        emptied = {0}  # dummy

        while emptied:
            added = set()
            emptied = set()

            for box in boxes:
                if status[box] or box in key_set:
                    num_candies += candies[box]
                    key_set |= set(keys[box])
                    added |= set(containedBoxes[box])
                    emptied.add(box)

            boxes |= added
            boxes -= emptied

        return num_candies
