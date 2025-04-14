# https://leetcode.com/problems/assign-elements-to-groups-with-constraints/


from collections import defaultdict


class Solution:
    # TLE
    def assignElements(self, groups: list[int], elements: list[int]) -> list[int]:
        indices_dict = defaultdict(list)
        for i, m in enumerate(groups):
            indices_dict[m].append(i)

        assigned = [-1] * len(groups)
        for m, indices in indices_dict.items():
            for j, n in enumerate(elements):
                if m % n:
                    continue

                for i in indices:
                    assigned[i] = j

                break

        return assigned

    def assignElements(self, groups: list[int], elements: list[int]) -> list[int]:
        max_size = max(groups)
        min_divisible_index = defaultdict(lambda: -1)

        for i, element in enumerate(elements):
            if element in min_divisible_index:
                continue

            for possible_size in range(element, max_size + 1, element):
                if possible_size in min_divisible_index:
                    continue

                min_divisible_index[possible_size] = i

        return [min_divisible_index[size] for size in groups]
