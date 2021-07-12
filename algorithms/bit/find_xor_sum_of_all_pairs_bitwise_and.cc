// https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and/

// time complexity: O(n)

#include <vector>

using namespace std;

class Solution {
public:
    int getXORSum(vector<int> &arr1, vector<int> &arr2) {
        int a = 0, b = 0;
        for (const auto &n : arr1)
            a ^= n;
        for (const auto &n : arr2)
            b ^= n;
        return a & b;
    }
};