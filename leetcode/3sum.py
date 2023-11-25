# https://leetcode.com/problems/3sum/

# time complexity: 

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplets = []
        if len(nums) < 3:
            return triplets
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                if (sum := nums[i] + nums[j] + nums[k]) == 0:
                    triplets.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k - 1] == nums[k]:
                        k -= 1
                    j += 1
                    k -= 1
                elif sum < 0:
                    j += 1
                else:
                    k -= 1
        return triplets