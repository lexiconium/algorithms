# https://leetcode.com/problems/minimum-number-of-refueling-stops/
# https://leetcode.com/problems/minimum-number-of-refueling-stops/discuss/149839/DP-O(N2)-and-Priority-Queue-O(NlogN)

# time complexity: O(n^2)

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        dp = [startFuel] + [0] * len(stations)
        for i, (position, fuel) in enumerate(stations, 1):
            for n in range(i)[::-1]:
                if dp[n] >= position:
                    dp[n + 1] = max(dp[n + 1], dp[n] + fuel)
        for n, dist in enumerate(dp):
            if dist >= target:
                return n
        return -1