// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/discuss/54118/C%2B%2B-Solution-with-O(n-%2B-klgn)-time-using-Max-Heap-and-Stack

// time complexity: O(n + klog(n))

#include <numeric>
#include <stack>
#include <vector>

using namespace std;

class Solution {
public:
    int maxProfit(int k, vector<int> &prices) {
        int max_profit = 0;
        int len = prices.size();
        int valley = 0; // valley index
        int peak = 0; // peak index + 1;

        vector<int> profits;
        stack<pair<int, int>> vp_pairs;
        while (peak < len) {
            for (valley = peak; valley < len - 1 && prices[valley] >= prices[valley + 1]; valley++);
            for (peak = valley + 1; peak < len && prices[peak] >= prices[peak - 1]; peak++);

            while (!vp_pairs.empty() && prices[valley] < prices[vp_pairs.top().first]) {
                profits.emplace_back(prices[vp_pairs.top().second - 1] - prices[vp_pairs.top().first]);
                vp_pairs.pop();
            }
            while (!vp_pairs.empty() && prices[peak - 1] >= prices[vp_pairs.top().second - 1]) {
                profits.emplace_back(prices[vp_pairs.top().second - 1] - prices[valley]);
                valley = vp_pairs.top().first;
                vp_pairs.pop();
            }
            vp_pairs.push({valley, peak});
        }
        while (!vp_pairs.empty()) {
            profits.emplace_back(prices[vp_pairs.top().second - 1] - prices[vp_pairs.top().first]);
            vp_pairs.pop();
        }
        if (k >= profits.size())
            max_profit = accumulate(profits.begin(), profits.end(), 0);
        else {
            nth_element(profits.begin(), profits.begin() + k, profits.end(), greater<int>());
            max_profit = accumulate(profits.begin(), profits.begin() + k, 0);
        }
        return max_profit;
    }
};