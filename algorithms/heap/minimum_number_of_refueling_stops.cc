// https://leetcode.com/problems/minimum-number-of-refueling-stops/
// https://leetcode.com/problems/minimum-number-of-refueling-stops/discuss/149839/DP-O(N2)-and-Priority-Queue-O(NlogN)

// time complexity: O(nlog(n))

#include <queue>
#include <vector>

using namespace std;

class Solution {
public:
    int minRefuelStops(int target, int startFuel, vector<vector<int>> &stations) {
        int fuel = startFuel, i = 0, len = stations.size(), n_refuel = 0;
        priority_queue<int> pq;
        for (; fuel < target; n_refuel++) {
            while (i < len && fuel >= stations[i][0])
                pq.push(stations[i++][1]);
            if (pq.empty())
                return -1;
            fuel += pq.top();
            pq.pop();
        }
        return n_refuel;
    }
};