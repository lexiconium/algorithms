// https://leetcode.com/problems/reorder-data-in-log-files/
// https://leetcode.com/problems/reorder-data-in-log-files/discuss/460589/98-Modern-C%2B%2B-using-STL-8-lines-of-code-with-detailed-explanation

// time complexity: O(nlog(n))

#include <algorithm>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    vector<string> reorderLogFiles(vector<string> &logs) {
        auto it = stable_partition(logs.begin(), logs.end(), [](const string &str) {
            return isalpha(str.back());
        });

        sort(logs.begin(), it, [](const string &str1, const string &str2) {
            auto substr1 = string(str1.begin() + str1.find(' '), str1.end());
            auto substr2 = string(str2.begin() + str2.find(' '), str2.end());
            return (substr1 == substr2) ? str1 < str2 : substr1 < substr2;
        });

        return logs;
    }
};