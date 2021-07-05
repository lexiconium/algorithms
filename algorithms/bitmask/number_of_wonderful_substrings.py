# https://leetcode.com/problems/number-of-wonderful-substrings/discuss/1299552/JavaC%2B%2BPython-Bit-Mask-%2B-Prefix

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        cnt_status = [1] + [0] * 1024
        cnt = idx = 0
        for c in word:
            idx ^= 1 << (ord(c) - ord('a'))
            cnt += cnt_status[idx] + sum(cnt_status[idx ^ (1 << n)] for n in range(10))
            cnt_status[idx] += 1
        return cnt