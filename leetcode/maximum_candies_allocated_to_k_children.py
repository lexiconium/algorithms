# https://leetcode.com/problems/maximum-candies-allocated-to-k-children/description/


from math import ceil


class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        if sum(candies) < k:
            return 0

        min_candies, max_candies = 1, max(candies)

        while min_candies < max_candies:
            n = ceil((min_candies + max_candies) / 2)
            num_divided = sum((num_candies // n) for num_candies in candies)

            if num_divided >= k:
                min_candies = n
            else:
                max_candies = n - 1

        return max_candies
