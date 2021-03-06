// https://leetcode.com/problems/valid-palindrome/

// time complexity: O(n)

#include <string>

using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        int len = s.length();
        int l = 0, r = len - 1;
        while (l < r) {
            while (l < r && !isalnum(s[l]))
                l++;
            while (l < r && !isalnum(s[r]))
                r--;
            if (tolower(s[l++]) != tolower(s[r--]))
                return false;
        }
        return true;
    }
};