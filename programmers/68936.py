def solution(arr):
    def can_compress(subarr):
        if len(subarr) == 1:
            return True

        target = subarr[0][0]

        return all(n == target for row in subarr for n in row)

    def divide_and_count(subarr):
        if can_compress(subarr):
            return (0, 1) if subarr[0][0] else (1, 0)

        half = len(subarr) // 2

        return tuple(map(sum, zip(
            divide_and_count([row[:half] for row in subarr[:half]]),
            divide_and_count([row[half:] for row in subarr[:half]]),
            divide_and_count([row[:half] for row in subarr[half:]]),
            divide_and_count([row[half:] for row in subarr[half:]]),
        )))

    return divide_and_count(arr)
