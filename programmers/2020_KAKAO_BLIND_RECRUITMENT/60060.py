# https://programmers.co.kr/learn/courses/30/lessons/60060

from collections import defaultdict

init_trie = lambda: defaultdict(init_trie)
trie_descendents_cnt = defaultdict(lambda: 0)

def cnt_word(trie, query):
    while True:
        if not query:
            return trie['cnt'] if 'cnt' in trie else 0
        if query[0] == '?':
            return trie_descendents_cnt[id(trie)]
    
        trie, query = trie[query[0]], query[1:]

def add_word(trie, word):
    while True:
        trie_descendents_cnt[id(trie)] += 1

        if not word:
            trie['is_terminal'] = True
            if 'cnt' in trie:
                trie['cnt'] += 1
            else:
                trie['cnt'] = 1
            return

        trie['is_branch'] = True
        trie, word = trie[word[0]], word[1:]

def solution(words, queries):
    prefix_tries = []
    suffix_tries = []
    for i in range(10001):
        prefix_tries.append(init_trie())
        suffix_tries.append(init_trie())
    
    for word in words:
        add_word(prefix_tries[len(word)], word)
        add_word(suffix_tries[len(word)], word[::-1])
    
    cnt_cache = {}
    cnts = []
    for query in queries:
        if query[0] != '?':
            try:
                cnt = cnt_cache[query]
            except:
                cnt = cnt_word(prefix_tries[len(query)], query)
                cnt_cache[query] = cnt
        else:
            try:
                cnt = cnt_cache[query]
            except:
                cnt = cnt_word(suffix_tries[len(query)], query[::-1])
                cnt_cache[query] = cnt
        cnts.append(cnt)
    return cnts
