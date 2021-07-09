// https://leetcode.com/problems/trapping-rain-water/

// time complexity: O(n)

#include <vector>

using namespace std;

class Solution {
public:
    int trap(vector<int> &height) {
        int len = height.size();
        if (len < 3)
            return 0;
        int volume = 0, left = 0, right = len - 1;
        int left_max = height[left], right_max = height[right];
        while (left < right) {
            if (left_max < right_max) {
                volume += left_max - height[left++];
                left_max = max(left_max, height[left]);
            } else {
                volume += right_max - height[right--];
                right_max = max(right_max, height[right]);
            }
        }
        return volume;
    }
};