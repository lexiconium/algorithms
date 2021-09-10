# https://programmers.co.kr/learn/courses/30/lessons/60060
# https://biewoom.github.io/coding%20test/kakao%202020%20blind/2020/04/13/search_lyrics.html

from collections import defaultdict

class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        curr = self.root
        while word:
            if word[0] not in curr:
                curr[word[0]] = [{} , 0]
            curr[word[0]][1] += 1

            curr = curr[word[0]][0]
            word = word[1:]

    def find(self, query)->int:
        curr = self.root
        prev_cnt = 0
        while query:
            if query[0] == '?':
                return prev_cnt
            if query[0] not in curr:
                return 0

            prev_cnt = curr[query[0]][1]
            curr = curr[query[0]][0]
            query = query[1:]

        return prev_cnt

def solution(words, queries):
    prefix_trie = defaultdict(Trie)
    suffix_trie = defaultdict(Trie)
    len_dict = defaultdict(int)
    result = []

    for word in words:
        prefix_trie[len(word)].insert(word)
        suffix_trie[len(word)].insert(word[::-1])
        len_dict[len(word)] += 1

    for query in queries:
        if query[0] == '?' and query[-1] == '?':
            result.append(len_dict[len(query)])
        elif query[0] != '?':
            result.append(prefix_trie[len(query)].find(query))
        else:
            result.append(suffix_trie[len(query)].find(query[::-1]))

    return result
