# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/

from collections import Counter, deque


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        word_len = len(words[0])
        num_words = len(words)

        words_counter = Counter(words)

        def get_starting_indices(begin_index: int) -> list[int]:
            starting_indices = []

            counter = Counter()
            q = deque([], maxlen=num_words)

            for i in range(begin_index, len(s), word_len):
                word = s[i : i + word_len]

                if word not in words_counter:
                    counter.clear()
                    q.clear()
                    continue

                counter[word] += 1
                q.append((i, word))

                if counter == words_counter:
                    starting_indices.append(q[0][0])

                if len(q) == num_words:
                    counter[q[0][1]] -= 1

            return starting_indices

        starting_indices = []

        for begin in range(word_len):
            starting_indices.extend(get_starting_indices(begin))

        return starting_indices
