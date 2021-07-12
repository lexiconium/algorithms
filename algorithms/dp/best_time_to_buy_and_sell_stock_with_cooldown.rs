// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75928/Share-my-DP-solution-(By-State-Machine-Thinking)

// time complexity: O(n)

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let (mut prev_sold, mut sold, mut hold, mut rest) = (0, 0, i32::MIN, 0);
        for p in &prices {
            prev_sold = sold;
            
            sold = hold + p;
            hold = std::cmp::max(hold, rest - p);
            rest = std::cmp::max(rest, prev_sold);
        }
        return std::cmp::max(sold, rest);
    }
}