import heapq


def cast(s):
    t, d = s.split()
    return int(t), ord(d) - ord("A")


instructions = [cast(input()) for _ in range(int(input()))]
passed = [-1 for _ in instructions]

roads = [[] for _ in range(4)]

t, idx = 0, 0
while True:
    if idx < len(instructions) and all(len(road) == 0 for road in roads):
        t = max(t, instructions[idx][0])

    f = False
    while idx < len(instructions) and t == instructions[idx][0]:
        heapq.heappush(roads[instructions[idx][1]], idx)
        idx += 1
        f = True

    if f and all(len(road) != 0 for road in roads):
        break

    d_passed = []
    for d, road in enumerate(roads):
        if not road:
            continue
        if roads[(d - 1) % 4]:
            continue

        passed[road[0]] = t
        d_passed.append(d)

    if not d_passed:
        break

    for d in d_passed:
        heapq.heappop(roads[d])

    t += 1

for _passed in passed:
    print(_passed)
