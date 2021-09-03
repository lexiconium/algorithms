# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/discuss/335668/DP-with-Bit-Masking-Solution-%3A-Best-for-Interviews

# time complexity: O(n2^n)

class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        if (_sum := sum(nums)) % k:
            return False
        
        nums.sort(reverse=True)
        _len, target = len(nums), _sum // k
        sums = [0] * (n_mask := 1 << _len)
        for mask in range(n_mask):
            if not mask or sums[mask]:
                for i in range(_len):
                    curr, prev = mask | 1 << i, mask
                    if curr != prev and sums[prev] % target + nums[i] <= target:
                        sums[curr] = sums[prev] + nums[i]
        return bool(sums[n_mask - 1])