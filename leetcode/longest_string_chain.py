# https://leetcode.com/problems/longest-string-chain/description/


class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        words = sorted(words, key=lambda s: len(s))

        dp = [1] * len(words)

        for i in reversed(range(len(words) - 1)):
            word_1 = words[i]
            for j in range(i + 1, len(words)):
                word_2 = words[j]

                if len(word_1) + 1 != len(word_2):
                    continue

                for k in range(len(word_2)):
                    if word_1 != word_2[:k] + word_2[k + 1:]:
                        continue

                    dp[i] = max(1 + dp[j], dp[i])
                    break

        return max(dp)

    def longestStrChain(self, words: list[str]) -> int:
        dp = {word: 1 for word in words}
        longest = 1

        for word in sorted(words, key=lambda s: len(s)):
            for i in range(len(word)):
                if (prev := word[:i] + word[i + 1:]) not in dp:
                    continue

                dp[word] = max(dp[prev] + 1, dp[word])
                longest = max(dp[word], longest)

        return longest
