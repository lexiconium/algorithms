# https://leetcode.com/problems/maximum-total-importance-of-roads/description/


import collections


class Solution:
    def maximumImportance(self, n: int, roads: list[list[int]]) -> int:
        num_connections = collections.Counter()

        for a, b in roads:
            num_connections[a] += 1
            num_connections[b] += 1

        total = 0

        for city, n_assigned in zip(
            sorted(
                num_connections, key=lambda city: num_connections[city], reverse=True
            ),
            range(n, 0, -1),
        ):
            total += num_connections[city] * n_assigned

        return total
