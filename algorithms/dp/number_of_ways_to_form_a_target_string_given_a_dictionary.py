# https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/
# https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/discuss/917779/JavaC%2B%2BPython-Space-O(N)

# time complexity: O(l(m + n)) where l: len(word), m: len(words), n: len(target)

from collections import Counter

class Solution:    
    def numWays(self, words: list[str], target: str) -> int:
        dp = [1] + [0] * (_len := len(target))
        for k in range(len(words[0])):
            cnt = Counter(word[k] for word in words)
            for i in range(_len)[::-1]:
                dp[i + 1] += dp[i] * cnt[target[i]]
        return dp[_len] % (10 ** 9 + 7)