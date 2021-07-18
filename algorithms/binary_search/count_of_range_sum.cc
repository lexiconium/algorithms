// https://leetcode.com/problems/count-of-range-sum/
// https://leetcode.com/problems/count-of-range-sum/discuss/77991/Short-and-simple-O(n-log-n)

// time complexity: O(nlog(n))

#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
    int len;
    int _lower, _upper;

public:
    int cnt_while_merge_sort(vector<long> &prefix_sums, int lo, int hi) {
        int mid = (lo + hi) / 2;
        if (mid == lo)
            return 0;

        int cnt = cnt_while_merge_sort(prefix_sums, lo, mid) + cnt_while_merge_sort(prefix_sums, mid, hi);

        int lbound = mid, ubound = mid;
        for (int i = lo; i < mid; i++) {
            while (lbound < hi && prefix_sums[lbound] - prefix_sums[i] < _lower)
                lbound++;
            while (ubound < hi && prefix_sums[ubound] - prefix_sums[i] <= _upper)
                ubound++;
            cnt += ubound - lbound;
        }

        sort(prefix_sums.begin() + lo, prefix_sums.begin() + hi);
        return cnt;
    }

    int countRangeSum(vector<int> &nums, int lower, int upper) {
        ios::sync_with_stdio(0);
        len = nums.size() + 1, _lower = lower, _upper = upper;
        vector<long> prefix_sums(len);
        for (int i = 1; i < len; i++)
            prefix_sums[i] += prefix_sums[i - 1] + nums[i - 1];
        return cnt_while_merge_sort(prefix_sums, 0, len);
    }
};