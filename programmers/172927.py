MINERALS = ["diamond", "iron", "stone"]
MINERAL_SCORES = {"diamond": 31, "iron": 6, "stone": 1}


def pick_used(pick, mineral):
    if pick == "diamond":
        return 1
    if pick == "iron":
        return 5 if mineral == "diamond" else 1
    if mineral == "diamond":
        return 25
    if mineral == "iron":
        return 5
    return 1


def solution(picks, minerals):
    pick_seq = []

    for i, mineral in enumerate(MINERALS):
        pick_seq.extend([mineral for _ in range(picks[i])])

    pick_seq = sorted(pick_seq, key=lambda pick: MINERAL_SCORES[pick], reverse=True)
    minerals = minerals[:min(len(pick_seq) * 5, len(minerals))]

    mineral_subsets = sorted(
        [minerals[i:min(i + 5, len(minerals))] for i in range(0, len(minerals), 5)],
        key=lambda subset: sum(MINERAL_SCORES[mineral] for mineral in subset),
        reverse=True
    )

    used = 0

    for pick, mineral_subset in zip(pick_seq, mineral_subsets):
        used += sum(pick_used(pick, mineral) for mineral in mineral_subset)

    return used
