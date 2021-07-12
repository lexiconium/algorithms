// https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and/

// time complexity: O(n)

impl Solution {
    pub fn get_xor_sum(arr1: Vec<i32>, arr2: Vec<i32>) -> i32 {
        let (mut a, mut b) = (0, 0);
        for n in &arr1 {
            a ^= n;
        }
        for n in &arr2 {
            b ^= n;
        }
        return a & b;
    }
}