// https://leetcode.com/problems/reverse-pairs/
// https://leetcode.com/problems/reverse-pairs/discuss/97287/C%2B%2B-with-iterators

// time complexity: O(nlog(n))

#include <vector>

using namespace std;

class Solution {
    int _len;

public:
    int merge_sort(vector<int>::iterator begin, vector<int>::iterator end) {
        _len = end - begin;
        if (_len < 2)
            return 0;

        auto mid = begin + _len / 2;
        int cnt = merge_sort(begin, mid) + merge_sort(mid, end);
        for (auto left = begin, right = mid; left < mid; left++) {
            while (right < end && (*left > 2L * *right))
                right++;
            cnt += right - mid;
        }
        inplace_merge(begin, mid, end);
        return cnt;
    }
    int reversePairs(vector<int> &nums) {
        return merge_sort(nums.begin(), nums.end());
    }
};