# https://leetcode.com/problems/minimum-operations-to-make-the-array-alternating/description/


import collections


class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0

        even_counter = collections.Counter()
        odd_counter = collections.Counter()

        num_odds = len(nums) // 2
        num_evens = num_odds + len(nums) % 2

        for i, n in enumerate(nums):
            if i % 2:
                odd_counter[n] += 1
            else:
                even_counter[n] += 1

        odd_values = sorted(odd_counter, key=lambda n: odd_counter[n], reverse=True)
        even_values = sorted(even_counter, key=lambda n: even_counter[n], reverse=True)

        odd_candidate = odd_values[0]
        even_candidate = even_values[0]

        num_odd_to_change = num_odds - odd_counter[odd_candidate]
        num_even_to_change = num_evens - even_counter[even_candidate]

        if odd_candidate == even_candidate:
            next_odd_count = odd_counter[odd_values[1]] if len(odd_values) > 1 else 0
            next_even_count = (
                even_counter[even_values[1]] if len(even_values) > 1 else 0
            )
            return min(
                num_odd_to_change + num_evens - next_even_count,
                num_odds - next_odd_count + num_even_to_change,
            )

        return num_odd_to_change + num_even_to_change

    def minimumOperations(self, nums: list[int]) -> int:
        pad = lambda x: x + [(None, 0)] * (2 - len(x))
        even = pad(collections.Counter(nums[::2]).most_common(2))
        odd = pad(collections.Counter(nums[1::2]).most_common(2))
        return len(nums) - (
            max(even[0][1] + odd[1][1], even[1][1] + odd[0][1])
            if even[0][0] == odd[0][0]
            else even[0][1] + odd[0][1]
        )
