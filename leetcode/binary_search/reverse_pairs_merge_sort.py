# https://leetcode.com/problems/reverse-pairs/
# https://leetcode.com/problems/reverse-pairs/discuss/97287/C%2B%2B-with-iterators

# time complexity: O(nlog(n))

class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        def merge_sort(begin: int, end: int) -> int:
            if end - begin < 2:
                return 0
            right = mid = (begin + end) // 2
            cnt = merge_sort(begin, mid) + merge_sort(mid, end)
            for left in range(begin, mid):
                while right < end and nums[left] > 2 * nums[right]:
                    right += 1
                cnt += right - mid
            nums[begin:end] = sorted(nums[begin:end])
            return cnt
        return merge_sort(0, len(nums))