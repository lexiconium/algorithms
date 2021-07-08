// https://leetcode.com/problems/two-sum/

// time complexity: O(n)

#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int> &nums, int target) {
        unordered_map<int, int> num_pairs;
        for (int i = 0; i < nums.size(); i++) {
            if (num_pairs.find(target - nums[i]) != num_pairs.end())
                return {i, num_pairs[target - nums[i]]};
            else
                num_pairs[nums[i]] = i;
        }
        return {-1};
    }
};