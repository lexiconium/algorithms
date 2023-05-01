# https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def dfs(begin: int = 0, substrings: set[str] = set()):
            if begin == len(s):
                return len(substrings)

            max_substrings = len(substrings)

            for end in range(begin + 1, len(s) + 1):
                if (substring := s[begin:end]) in substrings:
                    continue

                substrings.add(substring)
                max_substrings = max(dfs(end, substrings), max_substrings)
                substrings.remove(substring)

            return max_substrings

        return dfs()
