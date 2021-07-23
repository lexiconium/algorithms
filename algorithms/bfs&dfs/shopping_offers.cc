// https://leetcode.com/problems/shopping-offers/
// https://leetcode.com/problems/shopping-offers/discuss/105252/Concise-c%2B%2B-DFS-solution-6ms

// time complexity:

#include <numeric>
#include <vector>

using namespace std;

bool operator<(const vector<int> &to_check, const int condition) {
    for (const auto &n : to_check)
        if (n < condition)
            return true;
    return false;
}

void operator+=(vector<int> &left, const vector<int> &right) {
    for (int i = 0; i < left.size(); i++)
        left[i] += right[i];
}

void operator-=(vector<int> &left, const vector<int> &right) {
    for (int i = 0; i < left.size(); i++)
        left[i] -= right[i];
}

class Solution {
public:
    int shoppingOffers(vector<int> &price, vector<vector<int>> &special, vector<int> &needs) {
        if (needs < 0)
            return INT_MAX;

        long _min = inner_product(price.begin(), price.end(), needs.begin(), 0);
        for (const auto &offer : special) {
            if (offer.back() < _min) {
                needs -= offer;
                _min = min(_min, static_cast<long>(offer.back()) + shoppingOffers(price, special, needs));
                needs += offer;
            }
        }
        return static_cast<int>(_min);
    }
};