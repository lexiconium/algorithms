# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/description/


class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: list[str], groups: list[int]) -> list[str]:
        subsequence = [words[0]]
        group = groups[0]

        for i in range(1, n):
            if groups[i] == group:
                continue

            subsequence.append(words[i])
            group = groups[i]

        return subsequence
