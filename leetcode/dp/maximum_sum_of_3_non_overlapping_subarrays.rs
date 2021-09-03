// https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/

// time complexity: O(n)

impl Solution {
    pub fn max_sum_of_three_subarrays(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let k = k as usize;
        let (mut window1, mut window2, mut window3) = (0, 0, 0);
        for i in 0..k {
            window1 += nums[i];
            window2 += nums[i + k];
            window3 += nums[i + 2 * k];
        }
        let (mut max1, mut max2, mut max3) = (window1, window1 + window2, window1 + window2 + window3);
        let (mut idx1, mut idx2, mut idx3) = (0, [0, k], [0, k, 2 * k]);
        for i in k..nums.len() - 2 * k {
            window1 += nums[i] - nums[i - k];
            if window1 > max1 {
                max1 = window1;
                idx1 = i - k + 1;
            }
            window2 += nums[i + k] - nums[i];
            if max1 + window2 > max2 {
                max2 = max1 + window2;
                idx2 = [idx1, i + 1];
            }
            window3 += nums[i + 2 * k] - nums[i + k];
            if max2 + window3 > max3 {
                max3 = max2 + window3;
                idx3 = [idx2[0], idx2[1], i + k + 1];
            }
        }
        return vec![idx3[0] as i32, idx3[1] as i32, idx3[2] as i32];
    }
}