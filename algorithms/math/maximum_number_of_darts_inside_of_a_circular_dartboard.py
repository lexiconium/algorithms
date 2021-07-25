# https://leetcode.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/
# https://leetcode.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/discuss/636372/JavaC%2B%2BPython-POJ-1981

# time complexity: O(n^3)

import itertools

class Solution:
    def numPoints(self, points: list[list[int]], r: int) -> int:
        n_darts = 1
        for (x1, y1), (x2, y2) in itertools.combinations(points, 2):
            d2 = (x1 - x2) ** 2 + (y1 - y2) ** 2
            if d2 > 4 * (r2 := r ** 2):
                continue
            c2quad =  4 * r2 - d2
            xc = (x1 + x2) / 2 + (y1 - y2) * (c2quad / (4 * d2)) ** 0.5
            yc = (y1 + y2) / 2 + (x2 - x1) * (c2quad / (4 * d2)) ** 0.5
            # 1e-8 for floating point error
            # in theory, it should be <= r2
            n_darts = max(n_darts, sum((x - xc) ** 2 + (y - yc) ** 2 < r2 + 1e-8 for x, y in points))
        return n_darts