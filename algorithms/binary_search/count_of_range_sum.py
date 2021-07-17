# https://leetcode.com/problems/count-of-range-sum/

# time complexity: O(nlog(n))

import bisect

class Solution:
    def countRangeSum(self, nums: list[int], lower: int, upper: int) -> int:
        nums.insert(0, 0)
        prefix_sum = [0]
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
            prefix_sum.append(nums[i])
        prefix_sum.sort()
        
        cnt = 0
        for n in nums:
            del prefix_sum[bisect.bisect_left(prefix_sum, n)]
            cnt += bisect.bisect_right(prefix_sum, n + upper) - bisect.bisect_left(prefix_sum, n + lower)
        return cnt