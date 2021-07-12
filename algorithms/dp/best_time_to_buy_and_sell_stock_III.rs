// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/39611/Is-it-Best-Solution-with-O(n)-O(1).

// time complexity: O(n)

use std::cmp::max;

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let (mut bought1, mut bought2, mut sold1, mut sold2) = (i32::MIN, i32::MIN, 0, 0);
        for p in &prices {
            sold2 = max(sold2, bought2 + p);
            bought2 = max(bought2, sold1 - p);
            sold1 = max(sold1, bought1 + p);
            bought1 = max(bought1, -p);
        }
        return sold2;
    }
}