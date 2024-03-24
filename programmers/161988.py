def solution(sequence):
    for i in range(1, len(sequence)):
        sequence[i] = sequence[i - 1] + (-1 if i % 2 else 1) * sequence[i]

    sequence.append(0)

    return abs(max(sequence) - min(sequence))
