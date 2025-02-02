# https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/

import collections


class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        counter = collections.Counter()

        for word in words:
            counter += collections.Counter(word)

        n = len(words)

        for cnt in counter.values():
            if cnt % n:
                return False

        return True
