# https://leetcode.com/problems/corporate-flight-bookings/description/

import heapq
from itertools import accumulate


class Solution:
    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        bookings = sorted(bookings, reverse=True)

        lasts = []
        total, totals = 0, []

        for m in range(1, n + 1):
            while lasts and lasts[0][0] < m:
                last, seats = heapq.heappop(lasts)
                total -= seats

            while bookings and bookings[-1][0] <= m:
                first, last, seats = bookings.pop()
                total += seats

                heapq.heappush(lasts, (last, seats))

            totals.append(total)

        return totals

    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        diffs = [0 for _ in range(n + 1)]
        for first, last, seats in bookings:
            diffs[first - 1] += seats
            diffs[last] -= seats

        return list(accumulate(diffs))[:-1]
