# https://leetcode.com/problems/count-substrings-that-differ-by-one-character
# https://leetcode.com/problems/count-substrings-that-differ-by-one-character/solutions/917985/java-c-python-time-o-nm-space-o-1

class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        def compare(s_begin: int, t_begin: int) -> int:
            cnt = prev_cnt = curr_cnt = 0

            for l in range(min(len(s) - s_begin, len(t) - t_begin)):
                curr_cnt += 1

                if s[s_begin + l] != t[t_begin + l]:
                    prev_cnt, curr_cnt = curr_cnt, 0

                cnt += prev_cnt

            return cnt

        return (sum(compare(i, 0) for i in range(len(s)))
                + sum(compare(0, i) for i in range(1, len(t))))
