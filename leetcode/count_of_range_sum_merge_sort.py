# https://leetcode.com/problems/count-of-range-sum/
# https://leetcode.com/problems/count-of-range-sum/discuss/77991/Short-and-simple-O(n-log-n)

# time complexity: O(nlog(n))

class Solution:
    def countRangeSum(self, nums: list[int], lower: int, upper: int) -> int:
        prefix_sums = [0]
        for n in nums:
            prefix_sums.append(prefix_sums[-1] + n)
            
        def merge_sort(lo, hi):
            mid = (lo + hi) // 2
            if mid == lo:
                return 0
            cnt = merge_sort(lo, mid) + merge_sort(mid, hi)
            
            i = j = mid
            for pre_sum in prefix_sums[lo:mid]:
                while i < hi and prefix_sums[i] - pre_sum < lower:
                    i += 1
                while j < hi and prefix_sums[j] - pre_sum <= upper:
                    j += 1
                cnt += j - i
                
            prefix_sums[lo:hi] = sorted(prefix_sums[lo:hi])
            return cnt
        
        return merge_sort(0, len(prefix_sums))