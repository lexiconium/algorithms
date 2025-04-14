# https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/description/


class Solution:
    def minInsertions(self, s: str) -> int:
        num_rights = num_insertions = 0

        for p in s:
            match p:
                case "(":
                    num_rights += 2

                    if num_rights % 2:
                        num_rights -= 1
                        num_insertions += 1  # insert ")"

                case ")":
                    num_rights -= 1

                    # ")" came before "("
                    if num_rights < 0:
                        num_rights += 2
                        num_insertions += 1  # insert "("

                case _:
                    raise ValueError()

        return num_insertions + num_rights
