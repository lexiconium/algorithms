// https://leetcode.com/problems/burst-balloons/
// https://leetcode.com/problems/burst-balloons/discuss/76228/Share-some-analysis-and-explanations

// time complexity:

use std::cmp::max;

impl Solution {
    pub fn max_coins(nums: Vec<i32>) -> i32 {
        let mut nums = nums;
        nums.insert(0, 1);
        nums.push(1);
        let len = nums.len();

        let mut dp = vec![vec![0; len]; len - 1];
        for dist in 2..len {
            for i in 0..len - dist {
                let j = i + dist;
                for k in i + 1..j {
                    dp[i][j] = max(dp[i][j], dp[i][k] + nums[i] * nums[k] * nums[j] + dp[k][j]);
                }
            }
        }
        return dp[0][len - 1];
    }
}