// https://leetcode.com/problems/minimum-cost-to-merge-stones/submissions/
// https://leetcode.com/problems/minimum-cost-to-merge-stones/discuss/247567/JavaC%2B%2BPython-DP

// time complexity: O(n^3)

#include <vector>

using namespace std;

class Solution {
public:
    int mergeStones(vector<int> &stones, int k) {
        int len = stones.size();
        if ((len - 1) % (k - 1))
            return -1;
        
        vector<int> prefix_sum = vector<int>(len + 1);
        for (int i = 0; i < len; i++)
            prefix_sum[i + 1] = prefix_sum[i] + stones[i];
        
        vector<vector<int>> dp(len, vector<int>(len));
        for (int d = k; d <= len; d++) {
            for (int front = 0, back; front + d <= len; front++) {
                back = front + d - 1;
                dp[front][back] = INT_MAX;
                for (int i = front; i < back; i += k - 1)
                    dp[front][back] = min(dp[front][back], dp[front][i] + dp[i + 1][back]);
                if ((back - front) % (k - 1) == 0)
                    dp[front][back] += prefix_sum[back + 1] - prefix_sum[front];
            }
        }
        return dp[0][len - 1];
    }
};