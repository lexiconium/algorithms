def solution(s):
    num_conversion = 0
    removed_zeros = 0

    while s != "1":
        num_ones = sum(b == "1" for b in s)

        num_conversion += 1
        removed_zeros += len(s) - num_ones

        s = f"{num_ones:b}"

    return [num_conversion, removed_zeros]
