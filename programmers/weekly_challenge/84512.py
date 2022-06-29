# https://programmers.co.kr/learn/courses/30/lessons/84512

MAXLEN = 5
COMPONENTS = ["A", "E", "I", "O", "U"]


def solution(word: str):
    def count_words(_word: str):
        if _word > word:
            return 0
        if len(_word) == MAXLEN:
            return 1

        return 1 + sum(count_words(_word + c) for c in COMPONENTS)

    return sum(count_words(c) for c in COMPONENTS)
