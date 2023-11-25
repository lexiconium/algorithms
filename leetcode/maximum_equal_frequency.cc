// https://leetcode.com/problems/maximum-equal-frequency/
// https://leetcode.com/problems/maximum-equal-frequency/discuss/403743/JavaC%2B%2BPython-Only-2-Cases%3A-Delete-it-or-not

// time complexity: O(n)

#include <vector>

using namespace std;

class Solution {
public:
    int maxEqualFreq(vector<int> &nums) {
        int len = nums.size(), prefix_len = 0;
        vector<int> freq(1e5 + 1), cnt(len + 1);
        for (int i = 1, n, remainder; i <= len; i++) {
            n = nums[i - 1];
            cnt[freq[n]++]--;
            cnt[freq[n]]++;
            if (freq[n] * cnt[freq[n]] == i && i < len)
                prefix_len = i + 1;
            remainder = i - freq[n] * cnt[freq[n]];
            if (cnt[remainder] == 1 && (remainder == 1 || remainder == freq[n] + 1))
                prefix_len = i;
        }
        return prefix_len;
    }
};