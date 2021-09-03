// https://leetcode.com/problems/trapping-rain-water/

// time complexity: O(n)

#include <stack>
#include <vector>

using namespace std;

class Solution {
public:
    int trap(vector<int> &height) {
        int volume = 0;
        stack<int> stk;
        for (int i = 0, j, dist; i < height.size(); i++) {
            while (!stk.empty() && height[i] > height[stk.top()]) {
                j = stk.top();
                stk.pop();
                if (stk.empty())
                    break;
                dist = i - (stk.top() + 1);
                volume += (min(height[i], height[stk.top()]) - height[j]) * dist;
            }
            stk.push(i);
        }
        return volume;
    }
};