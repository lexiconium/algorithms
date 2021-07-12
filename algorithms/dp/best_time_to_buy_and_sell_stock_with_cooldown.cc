// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75928/Share-my-DP-solution-(By-State-Machine-Thinking)

// time complexity: O(n)

#include <vector>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int> &prices) {
        int prev_sold = 0, sold = 0, hold = INT32_MIN, rest = 0;
        for (const auto &p : prices) {
            prev_sold = sold;

            sold = hold + p;
            hold = max(hold, rest - p);
            rest = max(rest, prev_sold);
        }
        return max(sold, rest);
    }
};