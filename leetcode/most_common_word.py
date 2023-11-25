# https://leetcode.com/problems/most-common-word/

# time complexity:

import collections, re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        paragraph = [word for word in re.sub(r'[^\w]', ' ', paragraph.lower()).split() if word not in banned]
        return collections.Counter(paragraph).most_common(1)[0][0]