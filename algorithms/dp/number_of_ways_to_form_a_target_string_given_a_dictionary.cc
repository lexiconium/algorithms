// https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/
// https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/discuss/917779/JavaC%2B%2BPython-Space-O(N)

// time complexity: O(l(m + n)) where l: len(word), m: len(words), n: len(target)

#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int numWays(vector<string> &words, string target) {
        int len = target.length(), mod = 1e9 + 7;
        vector<long> dp(len + 1); dp[0] = 1;
        for (int i = 0; i < words[0].length(); i++) {
            vector<int> cnt(26);
            for (const auto &word : words)
                cnt[word[i] - 'a']++;
            for (int j = len - 1; j >= 0; j--)
                dp[j + 1] += dp[j] * cnt[target[j] - 'a'] % mod;
        }
        return dp[len] % mod;
    }
};