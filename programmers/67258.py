from collections import Counter
import heapq


def solution(gems):
    gem_types = set(gems)

    gem_counter = Counter()
    pq = []

    begin = 0

    for end, gem in enumerate(gems, 1):
        gem_counter[gem] += 1

        while len(gem_counter) == len(gem_types):
            gem_counter[(b_gem := gems[begin])] -= 1

            if not gem_counter[b_gem]:
                gem_counter.pop(b_gem)
                heapq.heappush(pq, (end - begin, begin + 1))

            begin += 1

    length, begin = heapq.heappop(pq)

    return [begin, begin + length - 1]
