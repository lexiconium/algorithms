// https://leetcode.com/problems/3sum/

// time complexity:

#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int> &nums) {
        int len = nums.size();
        if (len < 3)
            return {};

        vector<vector<int>> sums;
        sort(nums.begin(), nums.end());
        for (int i = 0, left, right, sum; i < len - 2; i++) {
            if (i > 0 && nums[i - 1] == nums[i])
                continue;

            left = i + 1, right = len - 1;
            while (left < right) {
                sum = nums[i] + nums[left] + nums[right];
                if (sum < 0)
                    left++;
                else if (sum > 0)
                    right--;
                else {
                    sums.push_back({nums[i], nums[left++], nums[right--]});
                    while (left < right && nums[left - 1] == nums[left])
                        left++;
                    while (left < right && nums[right] == nums[right + 1])
                        right--;
                }
            }
        }
        return sums;
    }
};