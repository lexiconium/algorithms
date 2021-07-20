# https://leetcode.com/problems/count-of-smaller-numbers-after-self/
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76584/Mergesort-solution

# time complexity: O(nlog(n))

class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        def merge_sort(enum: list[tuple[int, int]]) -> list[tuple[int, int]]:
            mid = (_len := len(enum)) // 2
            if mid:
                left, right = merge_sort(enum[:mid]), merge_sort(enum[mid:])
                for i in range(_len)[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        cnt[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum

        cnt = [0] * len(nums)
        merge_sort(list(enumerate(nums)))
        return cnt