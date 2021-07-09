// https://leetcode.com/problems/product-of-array-except-self/

// time complexity: O(n)

#include <vector>

using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int> &nums) {
        int len = nums.size();
        vector<int> multiplied(len);
        for (int i = 0, m = 1; i < len; i++) {
            multiplied[i] = m;
            m *= nums[i];
        }
        for (int i = len - 1, m = 1; i >= 0; i--) {
            multiplied[i] *= m;
            m *= nums[i];
        }
        return multiplied;
    }
};