// https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

// time complexity:

#include <numeric>
#include <vector>

using namespace std;

class Solution {
public:
    bool dfs(int k, int start, int curr) {
        if (curr == target)
            return k == 2 ? true : dfs(k - 1, 0, 0);

        for (int i = start; i < len; i++) {
            if (!used[i] && curr + _nums[i] <= target) {
                used[i] = true;
                if (dfs(k, i + 1, curr + _nums[i]))
                    return true;
                used[i] = false;
            }
        }
        return false;
    }

    bool canPartitionKSubsets(vector<int> &nums, int k) {
        int sum = accumulate(nums.begin(), nums.end(), 0);
        if (sum % k)
            return false;

        sort(nums.begin(), nums.end(), [](const auto &left, const auto &right) { return left < right; });
        len = nums.size(), target = sum / k;
        _nums = nums, used = vector<bool>(len);
        return dfs(k, 0, 0);
    }

private:
    vector<int> _nums;
    vector<bool> used;
    int len, target;
};