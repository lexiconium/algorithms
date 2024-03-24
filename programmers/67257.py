import re
from collections import deque
from itertools import permutations


def preprocess(expression):
    pattern = re.compile("[+\-*]")

    numbers = list(map(int, pattern.split(expression)))
    operations = pattern.findall(expression)

    return numbers, operations


def calc(numbers, operations, priority):
    numbers, operations = deque(numbers), deque(operations)

    for pop in priority:
        for _ in range(len(operations)):
            if operations[0] == pop:
                numbers.appendleft(
                    eval(f"{numbers.popleft()}{operations.popleft()}{numbers.popleft()}")
                )
            else:
                numbers.rotate(-1)
                operations.rotate(-1)

        numbers.rotate(-1)

    return abs(numbers[0])


def solution(expression):
    numbers, operations = preprocess(expression)
    return max(calc(numbers, operations, priority) for priority in permutations("+-*"))
