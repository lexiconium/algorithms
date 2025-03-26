# https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/description/


from collections import Counter


class Solution:
    def digitCount(self, num: str) -> bool:
        counter = Counter(num)

        for i, c in enumerate(num):
            if counter[str(i)] != int(c):
                return False

        return True
