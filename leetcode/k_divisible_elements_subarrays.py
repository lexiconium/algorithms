# https://leetcode.com/problems/k-divisible-elements-subarrays/


class TrieNode:
    def __init__(self):
        self.children = {}


class Solution:
    def countDistinct(self, nums: list[int], k: int, p: int) -> int:
        subarrays = set()

        for begin in range(n := len(nums)):
            subarr = tuple()
            num_divisible = 0

            for i in range(begin, n):
                subarr += (num := nums[i],)
                num_divisible += num % p == 0

                if num_divisible > k:
                    break

                subarrays.add(subarr)

        return len(subarrays)

    # Trie; o1-mini
    def countDistinct(self, nums: list[int], k: int, p: int) -> int:
        root = TrieNode()
        count = 0

        for i in range(len(nums)):
            current = root
            count_div_p = 0

            for j in range(i, len(nums)):
                if nums[j] % p == 0:
                    count_div_p += 1

                if count_div_p > k:
                    break

                if nums[j] not in current.children:
                    current.children[nums[j]] = TrieNode()
                    count += 1

                current = current.children[nums[j]]

        return count
