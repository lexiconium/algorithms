// https://leetcode.com/problems/most-common-word/
// https://leetcode.com/problems/most-common-word/discuss/123854/C%2B%2BJavaPython-Easy-Solution-with-Explanation

// time complexity:

#include <sstream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
public:
    string mostCommonWord(string p, vector<string> &banned) {
        unordered_set<string> ban(banned.begin(), banned.end());
        unordered_map<string, int> count;
        for (auto &c : p)
            c = isalpha(c) ? tolower(c) : ' ';
        istringstream iss(p);
        string w;
        pair<string, int> most_common("", 0);
        while (iss >> w)
            if (ban.find(w) == ban.end() && ++count[w] > most_common.second)
                most_common = make_pair(w, count[w]);
        return most_common.first;
    }
};