# https://leetcode.com/problems/minimum-number-of-refueling-stops/
# https://leetcode.com/problems/minimum-number-of-refueling-stops/discuss/149839/DP-O(N2)-and-Priority-Queue-O(NlogN)

# time complexity: O(nlog(n))

import heapq

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        n_refuel, i, fuel = 0, 0, startFuel
        pq = []
        while fuel < target:
            while i < len(stations) and fuel >= stations[i][0]:
                heapq.heappush(pq, -stations[i][1])
                i += 1
            if not pq:
                return -1
            fuel -= heapq.heappop(pq)
            n_refuel += 1
        return n_refuel