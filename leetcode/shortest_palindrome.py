# https://leetcode.com/problems/shortest-palindrome/submissions/

# time complexity:

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if (l := len(s)) < 2 or (r := s[::-1]) == s:
            return s
        j = 0
        for i in range(l - 1, -1, -1):
            j += s[i] == s[j]
        return r[:l - j] + self.shortestPalindrome(s[:j]) + s[j:]