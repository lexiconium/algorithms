// https://leetcode.com/problems/maximum-product-subarray/
// https://leetcode.com/problems/maximum-product-subarray/discuss/183483/JavaC%2B%2BPython-it-can-be-more-simple

// time complexity: O(n)

#include <vector>

using namespace std;

class Solution {
public:
    int maxProduct(vector<int> &nums) {
        int len = nums.size(), max_p = INT32_MIN, l = 0, r = 0;
        for (int i = 0; i < len; i++) {
            l = (l ? l : 1) * nums[i];
            r = (r ? r : 1) * nums[len - 1 - i];
            max_p = max(max_p, max(l, r));
        }
        return max_p;
    }
};