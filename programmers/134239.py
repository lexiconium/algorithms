def get_sequence(n):
    if n == 1:
        return (1,)
    return n, *get_sequence(3 * n + 1 if n % 2 else n // 2)


def solution(k, ranges):
    sequence = get_sequence(k)

    prefix_sums = [0] + [(sequence[i] + sequence[i + 1]) / 2 for i in range(len(sequence) - 1)]

    for i in range(len(prefix_sums) - 1):
        prefix_sums[i + 1] += prefix_sums[i]

    return [
        prefix_sums[end - 1] - prefix_sums[begin] if begin < len(prefix_sums) + end else -1
        for begin, end in ranges
    ]
