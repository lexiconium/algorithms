from collections import defaultdict


def solution(friends, gifts):
    info = defaultdict(
        lambda: {"in": defaultdict(int), "out": defaultdict(int), "index": 0}
    )

    for from_to in gifts:
        name_1, name_2 = from_to.split(" ")

        info[name_1]["out"][name_2] += 1
        info[name_1]["index"] += 1

        info[name_2]["in"][name_1] += 1
        info[name_2]["index"] -= 1

    receives = [0] * len(friends)

    for i in range(len(friends) - 1):
        name_1 = friends[i]

        for j in range(i + 1, len(friends)):
            if (out_1 := info[name_1]["out"][(name_2 := friends[j])]) > (
                out_2 := info[name_2]["out"][name_1]
            ):
                receives[i] += 1
            elif out_1 < out_2:
                receives[j] += 1
            elif (index_1 := info[name_1]["index"]) > (
                index_2 := info[name_2]["index"]
            ):
                receives[i] += 1
            elif index_1 < index_2:
                receives[j] += 1

    return max(receives)
