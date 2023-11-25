# https://leetcode.com/problems/longest-palindromic-substring/

# time complexity: O(nm)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s == s[::-1]:
            return s

        def widen(left : int, right : int) -> str:
            while left > 0 and right < len(s) - 1 and s[left - 1] == s[right + 1]:
                left -= 1
                right += 1
            return s[left:right + 1]

        palindrome = ''
        i = 0
        while i < len(s):
            left, right = i, i
            while right < len(s) - 1 and s[right] == s[right + 1]:
                right += 1
            i = right + 1
            palindrome = max(palindrome, widen(left, right), key=len)
        return palindrome