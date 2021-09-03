# https://leetcode.com/problems/minimum-cost-to-merge-stones/submissions/
# https://leetcode.com/problems/minimum-cost-to-merge-stones/discuss/247567/JavaC%2B%2BPython-DP

# time complexity: O(n^3)

from functools import cache

class Solution:
    def mergeStones(self, stones: list[int], k: int) -> int:
        _len = len(stones)
        if (_len - 1) % (k - 1):
            return -1
        
        prefix_sum = [0] * (_len + 1)
        for i, n in enumerate(stones):
            prefix_sum[i + 1] = prefix_sum[i] + n

        @cache
        def dp(front, back):
            if back - front + 1 < k:
                return 0
            _min = min(dp(front, i) + dp(i + 1, back) for i in range(front, back, k - 1))
            if not (back - front) % (k - 1):
                _min += prefix_sum[back + 1] - prefix_sum[front]
            return _min
        
        return dp(0, _len - 1)