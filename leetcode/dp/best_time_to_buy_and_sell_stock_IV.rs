// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

// time complexity: O(kn)

use std::cmp::max;

impl Solution {
    pub fn max_profit(k: i32, prices: Vec<i32>) -> i32 {
        let k = k as usize;
        let (mut bought, mut sold) = (vec![i32::MIN; k + 1], vec![0; k + 1]);
        for p in &prices {
            for i in 1..k + 1 {
                sold[i] = max(sold[i], bought[i] + p);
                bought[i] = max(bought[i], sold[i - 1] - p);
            }
        }
        return sold[k];
    }
}