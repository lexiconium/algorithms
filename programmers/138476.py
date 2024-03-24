from collections import Counter


def solution(k, tangerine):
    counter = Counter(tangerine)

    num_sizes = 0
    nums = 0

    for size, n in counter.most_common(len(counter)):
        nums += n
        num_sizes += 1

        if nums >= k:
            break

    return num_sizes
