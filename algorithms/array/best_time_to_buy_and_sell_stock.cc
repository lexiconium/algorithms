// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

// time complexity: O(n)

#include <vector>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int> &prices) {
        int min_p = INT32_MAX, profit = 0;
        for (const auto &p : prices) {
            min_p = min(min_p, p);
            profit = max(profit, p - min_p);
        }
        return profit;
    }
};