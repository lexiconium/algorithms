import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        return (s := re.sub('[^a-z0-9]', '', s.lower())) == s[::-1]