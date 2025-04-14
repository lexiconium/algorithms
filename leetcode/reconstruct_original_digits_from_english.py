# https://leetcode.com/problems/reconstruct-original-digits-from-english/description/


import collections


class Solution:
    def originalDigits(self, s: str) -> str:
        num_to_digit = {
            "zero": 0,
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
        }
        num_to_id = {
            "zero": "z",
            "one": "1o",
            "two": "w",
            "three": "1h",
            "four": "u",
            "five": "1f",
            "six": "x",
            "seven": "2v",
            "eight": "g",
            "nine": "3i",
        }
        order = [
            "zero",
            "two",
            "four",
            "six",
            "eight",
            "one",
            "three",
            "five",
            "seven",
            "nine",
        ]

        counter = collections.Counter(s)
        digits = []

        for num in order:
            cnt = counter[num_to_id[num][-1]]

            if not cnt:
                continue

            digits.extend([num_to_digit[num]] * cnt)

            for c in num:
                counter[c] -= cnt

        return "".join(map(str, sorted(digits)))
