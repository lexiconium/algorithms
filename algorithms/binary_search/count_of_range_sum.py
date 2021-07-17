# https://leetcode.com/problems/count-of-range-sum/

# time complexity: O(nlog(n))

class Solution:
    def countRangeSum(self, nums: list[int], lower: int, upper: int) -> int:
        sum_n_elements = [0]
        for n in nums:
            sum_n_elements.append(sum_n_elements[-1] + n)

        def merge_sort(lo, hi):
            mid = (lo + hi) // 2
            if mid == lo:
                return 0
            cnt = merge_sort(lo, mid) + merge_sort(mid, hi)
            
            i = j = mid
            for left in sum_n_elements[lo:mid]:
                while i < hi and sum_n_elements[i] - left < lower:
                    i += 1
                while j < hi and sum_n_elements[j] - left <= upper:
                    j += 1
                cnt += j - 1
            
            sum_n_elements[lo:hi] = sorted(sum_n_elements[lo:hi])
            return cnt
        
        return merge_sort(0, len(sum_n_elements))