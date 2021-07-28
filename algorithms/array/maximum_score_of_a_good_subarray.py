# https://leetcode.com/problems/maximum-score-of-a-good-subarray/

# time complexity: O(n)

class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:
        _min, _max, _len = nums[k], nums[k], len(nums)
        i = j = k
        while i > 0 or j + 1 < _len:
            if (nums[i - 1] if i else 0) > (nums[j + 1] if j + 1 < _len else 0):
                i -= 1
            else:
                j += 1
            _min = min(_min, nums[i], nums[j])
            _max = max(_max, _min * (j - i + 1))
        return _max