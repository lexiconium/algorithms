// https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/

// time complexity: O(n)

#include <numeric>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> maxSumOfThreeSubarrays(vector<int> &nums, int k) {
        int window1 = accumulate(nums.begin(), nums.begin() + k, 0);
        int window2 = accumulate(nums.begin() + k, nums.begin() + 2 * k, 0);
        int window3 = accumulate(nums.begin() + 2 * k, nums.begin() + 3 * k, 0);

        int max1 = window1, max2 = window1 + window2, max3 = window1 + window2 + window3;
        int idx1 = 0;
        vector<int> idx2 = {0, k}, idx3 = {0, k, 2 * k};

        for (int i = k; i < nums.size() - 2 * k; i++) {
            window1 += nums[i] - nums[i - k];
            if (window1 > max1) {
                max1 = window1;
                idx1 = i - k + 1;
            }
            window2 += nums[i + k] - nums[i];
            if (max1 + window2 > max2) {
                max2 = max1 + window2;
                idx2 = {idx1, i + 1};
            }
            window3 += nums[i + 2 * k] - nums[i + k];
            if (max2 + window3 > max3) {
                max3 = max2 + window3;
                idx3 = {idx2[0], idx2[1], i + k + 1};
            }
        }
        return idx3;
    }
};