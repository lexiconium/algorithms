// https://leetcode.com/problems/minimum-number-of-refueling-stops/
// https://leetcode.com/problems/minimum-number-of-refueling-stops/discuss/149839/DP-O(N2)-and-Priority-Queue-O(NlogN)

// time complexity: O(n^2)

#include <vector>

using namespace std;

class Solution {
public:
    int minRefuelStops(int target, int startFuel, vector<vector<int>> &stations) {
        int n_stations = stations.size();
        vector<long> dp(n_stations + 1);
        dp[0] = startFuel;
        for (int i = 0; i < n_stations; i++) {
            for (int n_refuel = i; n_refuel >= 0; n_refuel--) {
                if (dp[n_refuel] >= stations[i][0])
                    dp[n_refuel + 1] = max(dp[n_refuel + 1], dp[n_refuel] + stations[i][1]);
            }
        }
        for (int n_refuel = 0; n_refuel < n_stations + 1; n_refuel++)
            if (dp[n_refuel] >= target)
                return n_refuel;
        return -1;
    }
};