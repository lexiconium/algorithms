// https://leetcode.com/problems/shortest-palindrome/submissions/

// time complexity:

#include <string>

using namespace std;

class Solution {
public:
    string shortestPalindrome(string s) {
        int len = s.length();
        auto r = s;
        reverse(r.begin(), r.end());
        if (len < 2 || r == s)
            return s;
        int j = 0;
        for (int i = len - 1; i >= 0; i--)
            j += s[i] == s[j];
        return r.substr(0, len - j).append(shortestPalindrome(s.substr(0, j))).append(s.substr(j, len - j));
    }
};