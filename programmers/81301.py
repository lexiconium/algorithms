def solution(s):
    digits = []
    tmp = ""

    to_digit = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9",
    }

    for c in s:
        if c.isdigit():
            digits.append(c)
        else:
            tmp += c

            if tmp in to_digit:
                digits.append(to_digit[tmp])
                tmp = ""

    return int("".join(digits))
