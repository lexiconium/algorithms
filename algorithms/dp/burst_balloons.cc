// https://leetcode.com/problems/burst-balloons/
// https://leetcode.com/problems/burst-balloons/discuss/76228/Share-some-analysis-and-explanations

// time complexity:

#include <vector>

using namespace std;

class Solution {
public:
    int maxCoins(vector<int>& nums) {
        nums.insert(nums.begin(), 1);
        nums.emplace_back(1);
        int len = nums.size();
        
        vector<vector<int>> dp(len - 1, vector<int>(len, 0));
        for (int d = 2; d < len; d++) {
            for (int i = 0, j; i < len - d; i++) {
                j = i + d;
                for (int k = i + 1; k < j; k++)
                    dp[i][j] = max(dp[i][j], dp[i][k] + nums[i] * nums[k] * nums[j] + dp[k][j]);
            }
        }
        return dp[0][len - 1];
    }
};