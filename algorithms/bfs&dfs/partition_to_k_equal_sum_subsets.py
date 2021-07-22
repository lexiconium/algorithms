# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

# time complexity:

class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        if (_sum := sum(nums)) % k:
            return False
        
        nums.sort(reverse=True)
        used, target = [False] * (_len := len(nums)), _sum // k

        def dfs(k, start, curr):
            if curr == target:
                return True if k == 2 else dfs(k - 1, 0, 0)

            for i in range(start, _len):
                if not used[i] and curr + nums[i] <= target:
                    used[i] = True
                    if dfs(k, i + 1, curr + nums[i]):
                        return True
                    used[i] = False
            return False
        
        return dfs(k, 0, 0)

# Though it's slow due to repeating visits, an alternative solution:
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/discuss/108741/Solution-with-Reference

    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        if (_sum := sum(nums)) % k:
            return False
        
        partition = [_sum // k] * k
        _len = len(nums)
        nums.sort(reverse=True)
        
        def dfs(idx: int) -> bool:
            if idx == _len:
                return True
            for i, p in enumerate(partition):
                if p >= nums[idx]:
                    partition[i] -= nums[idx]
                    if dfs(idx + 1):
                        return True
                    partition[i] += nums[idx]
            return False
        return dfs(0)