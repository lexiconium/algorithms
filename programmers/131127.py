from collections import Counter


def solution(want, number, discount):
    want_counter = Counter()

    for item, num_items in zip(want, number):
        want_counter[item] = num_items

    discount_counter = Counter(discount[:9])
    cnt = 0

    for i, item in enumerate(discount[9:]):
        discount_counter[item] += 1

        if not discount_counter - want_counter:
            cnt += 1

        discount_counter[discount[i]] -= 1

    return cnt
