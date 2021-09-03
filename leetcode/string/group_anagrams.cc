// https://leetcode.com/problems/group-anagrams/submissions/

// time complextiry: O(nmlog(m))

#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string> &strs) {
        unordered_map<string, vector<string>> anagrams;
        for (string &word : strs) {
            string w = word;
            sort(word.begin(), word.end());
            anagrams[word].emplace_back(w);
        }
        vector<vector<string>> ret;
        for_each(anagrams.begin(), anagrams.end(), [&ret](auto &entry) { ret.emplace_back(entry.second); });
        return ret;
    }
};