def is_unique(column):
    return len(set(column)) == len(column)


def solution(relation):
    candidates = []

    columns = list(zip(*relation))

    for cand_comb in range(1, 1 << len(columns)):
        if not is_unique(list(zip(*[columns[index] for index in range(len(columns)) if cand_comb & (1 << index)]))):
            continue

        if any(key_comb & cand_comb == key_comb for key_comb in candidates):
            continue

        candidates.append(cand_comb)

    return len(candidates)
