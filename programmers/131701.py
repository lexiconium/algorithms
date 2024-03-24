def solution(elements):
    prefix_sums = elements[:]

    for i in range(len(prefix_sums) - 1):
        prefix_sums[i + 1] += prefix_sums[i]

    possibles = set()

    for len_subset in range(1, len(elements) + 1):
        for i in range(len(elements)):
            subset_sum = prefix_sums[i] - prefix_sums[(j := i - len_subset)]

            if j < 0:
                subset_sum += prefix_sums[-1]

            possibles.add(subset_sum)

    return len(possibles)


def solution(elements):
    possibles = set()

    for i in range(len_elements := len(elements)):
        subset_sum = 0

        for j in range(i, i + len_elements):
            possibles.add(subset_sum := subset_sum + elements[j % len_elements])

    return len(possibles)
