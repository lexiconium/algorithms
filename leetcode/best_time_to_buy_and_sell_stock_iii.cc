// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/39611/Is-it-Best-Solution-with-O(n)-O(1).

// time complexity: O(n)

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        ios::sync_with_stdio(0);
        
        int bought1 = INT32_MIN, bought2 = INT32_MIN;
        int sold1 = 0, sold2 = 0;
        for (const auto &p : prices) {
            sold2 = max(sold2, bought2 + p);
            bought2 = max(bought2, sold1 - p);
            sold1 = max(sold1, bought1 + p);
            bought1 = max(bought1, -p);
        }
        return sold2;
    }
};