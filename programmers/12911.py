def solution(n):
    max_digit = 0

    while n > (1 << max_digit):
        max_digit += 1

    digits_before_zero = []
    zero_digit = -1

    for exp in range(max_digit + 1):
        is_one = n & (1 << exp)

        if is_one:
            digits_before_zero.append(exp)
        elif digits_before_zero:
            zero_digit = exp
            break

    n += 1 << (max_digit + 1 if zero_digit == -1 else zero_digit)
    n -= sum(1 << digit for digit in digits_before_zero)
    n += sum(1 << digit for digit in range(len(digits_before_zero) - 1))

    return n
