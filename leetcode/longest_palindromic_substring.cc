// https://leetcode.com/problems/longest-palindromic-substring/

// time complexity: O(nm)

#include <string>

using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        int len = s.length();
        if (len == 1 || s == string(s.rbegin(), s.rend()))
            return s;
        string longest, substr;
        int i = 0, left, right;
        while (i < len) {
            left = right = i;
            while (right < len - 1 && s[right] == s[right + 1])
                right++;
            i = right + 1;
            while (left > 0 && right < len - 1 && s[left - 1] == s[right + 1]) {
                left--;
                right++;
            }
            substr = s.substr(left, right - left + 1);
            longest = longest.length() > substr.length() ? longest : substr;
        }
        return longest;
    }
};