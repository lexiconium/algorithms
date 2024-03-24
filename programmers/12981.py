def solution(n, words):
    seen = set()
    prev_word = words[0][0]

    for i, word in enumerate(words):
        if word in seen or word[0] != prev_word[-1]:
            return list(map(lambda x: x + 1, divmod(i, n)))[::-1]

        seen.add(word)
        prev_word = word

    return [0, 0]
